#!/usr/bin/env bash
# neutralize-db.sh — neutralise a database restored from production into a local or stage Docker instance,
# then verify it, so that it can never reach the organisation's real systems (mail, crons, payments).
#
#   $(texo where --pack odoo_partner)/scripts/neutralize-db.sh <stack dir> <db>
#     <stack dir>  folder with the instance's docker-compose.yml (e.g. odoo/odoo-clients/<slug>-v19)
#     <db>         database to neutralise (e.g. <slug>-local)
#
# (a) runs Odoo's own `odoo neutralize` in a one-off web container, through the official image entrypoint
#     (which passes the database connection from HOST/USER/PASSWORD), bypassing any custom entrypoint;
# (b) checks read-only with psql that the database is marked neutralised and that no mail server, incoming
#     mail server, live payment provider or cron of a non-Odoo module is still active. Any failure exits 1: do not start the instance.
# Neutralising is not anonymising: for organisations that serve vulnerable people the personal data must
# also be anonymised before anyone works on the database (anonymize-db.sh, next to this script).
#
# Variables: WEB_SERVICE (default web), DB_SERVICE (default db), ODOO_CONF (default /etc/odoo/odoo.conf),
# PGUSER (default odoo).
set -euo pipefail

STACK_DIR="${1:?usage: neutralize-db.sh <stack dir> <db>}"
DB="${2:?usage: neutralize-db.sh <stack dir> <db>}"
COMPOSE="${STACK_DIR%/}/docker-compose.yml"
WEB="${WEB_SERVICE:-web}"
DBS="${DB_SERVICE:-db}"
CONF="${ODOO_CONF:-/etc/odoo/odoo.conf}"
PGU="${PGUSER:-odoo}"

[ -f "$COMPOSE" ] || { echo "[fatal] compose not found: $COMPOSE" >&2; exit 2; }
case "$DB" in *prod*) echo "[fatal] refusing a database whose name says production: $DB" >&2; exit 2 ;; esac

echo "--> odoo neutralize on ${DB}"
docker compose -f "$COMPOSE" run --rm -T --no-deps --entrypoint /entrypoint.sh "$WEB" odoo neutralize -c "$CONF" -d "$DB" --stop-after-init

q() {   # q <sql>: one value, in a read-only transaction
    docker compose -f "$COMPOSE" exec -T -e PGOPTIONS="-c default_transaction_read_only=on" "$DBS" \
        psql -U "$PGU" -d "$DB" -tAX -v ON_ERROR_STOP=1 -c "$1"
}
count_if_table() {   # count_if_table <table> <where>: 0 when the table does not exist (module not installed)
    if [ "$(q "SELECT to_regclass('public.$1') IS NOT NULL")" = "t" ]; then
        q "SELECT count(*) FROM $1 WHERE $2"
    else
        echo 0
    fi
}

echo "--> verify"
fail=0
check() {   # check <label> <value> <expected>
    if [ "$2" = "$3" ]; then echo "    [ok] $1"; else echo "    [FAIL] $1: $2 (expected $3)"; fail=1; fi
}
check "database marked as neutralised" \
    "$(q "SELECT coalesce((SELECT lower(value) FROM ir_config_parameter WHERE key = 'database.is_neutralized'), 'missing')")" "true"
# Odoo's neutralize adds an active server with host 'invalid' that swallows every email: that one is wanted.
check "active outgoing mail servers" "$(count_if_table ir_mail_server "active AND smtp_host <> 'invalid'")" "0"
check "active incoming mail servers" "$(count_if_table fetchmail_server "active")" "0"
check "live payment providers" "$(count_if_table payment_provider "state = 'enabled'")" "0"
check "active crons of non-Odoo modules" "$(q "SELECT count(*) FROM ir_cron c JOIN ir_model_data d
    ON d.model = 'ir.cron' AND d.res_id = c.id WHERE c.active AND d.module NOT IN
    (SELECT name FROM ir_module_module WHERE author ILIKE '%Odoo S.A.%')")" "0"

if [ "$fail" -ne 0 ]; then
    echo "[fail] ${DB} is NOT safe: do not start the instance on it." >&2
    exit 1
fi
echo "[ok] ${DB} neutralised and verified."
