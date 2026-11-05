#!/usr/bin/env bash
# anonymize-db.sh — neutralise, anonymise and verify a copy of a production database in a local Docker instance.
#
#   $(texo where --pack odoo_partner)/scripts/anonymize-db.sh <stack dir> <db> [admin password]
#
# 1. neutralize-db.sh (Odoo's neutralize plus checks): stops here if it fails;
# 2. anonymize-db.sql: people's names, contacts, addresses, messages, stored files, OAuth tokens, API keys,
#    e-invoicing keys and backup credentials removed or replaced with fake values;
# 3. read-only checks: any person's data left exits 1 — do not start the instance on that database;
# 4. the admin user (id 2) gets login `admin` and the given password (default `admin`), for local use only.
# For organisations that serve vulnerable people this is the minimum before anyone works on a copy.
#
# Variables: as neutralize-db.sh (WEB_SERVICE, DB_SERVICE, ODOO_CONF, PGUSER).
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STACK_DIR="${1:?usage: anonymize-db.sh <stack dir> <db> [admin password]}"
DB="${2:?usage: anonymize-db.sh <stack dir> <db> [admin password]}"
ADMIN_PASSWORD="${3:-admin}"
COMPOSE="${STACK_DIR%/}/docker-compose.yml"
WEB="${WEB_SERVICE:-web}"
DBS="${DB_SERVICE:-db}"
CONF="${ODOO_CONF:-/etc/odoo/odoo.conf}"
PGU="${PGUSER:-odoo}"

bash "$HERE/neutralize-db.sh" "$STACK_DIR" "$DB"

echo "--> anonymise ${DB}"
docker compose -f "$COMPOSE" exec -T "$DBS" psql -U "$PGU" -d "$DB" -q -v ON_ERROR_STOP=1 \
    < "$HERE/anonymize-db.sql" 2>&1 | sed -n 's/^.*NOTICE:  /    /p'

q() {   # q <sql>: one value, in a read-only transaction
    docker compose -f "$COMPOSE" exec -T -e PGOPTIONS="-c default_transaction_read_only=on" "$DBS" \
        psql -U "$PGU" -d "$DB" -tAX -v ON_ERROR_STOP=1 -c "$1"
}
n() {   # n <table> <where>: rows matching, 0 when the table does not exist
    if [ "$(q "SELECT to_regclass('public.$1') IS NOT NULL")" = "t" ]; then
        q "SELECT count(*) FROM $1 WHERE $2"
    else
        echo 0
    fi
}
fail=0
check() {   # check <label> <value> <expected>
    if [ "$2" = "$3" ]; then echo "    [ok] $1"; else echo "    [FAIL] $1: $2 (expected $3)"; fail=1; fi
}
echo "--> verify"
keep="SELECT partner_id FROM res_company UNION SELECT res_id FROM ir_model_data WHERE model = 'res.partner' AND module = 'base' AND name IN ('partner_root', 'public_partner')"
check "partners with a real email" "$(n res_partner "id NOT IN ($keep) AND email IS NOT NULL AND email NOT LIKE '%@example.invalid'")" "0"
check "partners with a phone" "$(n res_partner "id NOT IN ($keep) AND phone IS NOT NULL")" "0"
check "partners with a real name" "$(n res_partner "id NOT IN ($keep) AND name !~ '^(Persona|Organizzazione) [0-9]+\$'")" "0"
check "users with a real login" "$(n res_users "id <> 2 AND login NOT LIKE '%@example.invalid'")" "0"
check "messages" "$(n mail_message "true")" "0"
check "stored files" "$(n ir_attachment "store_fname IS NOT NULL OR db_datas IS NOT NULL")" "0"
check "event registrations with a real email" "$(n event_registration "email IS NOT NULL AND email NOT LIKE '%@example.invalid'")" "0"
check "API keys" "$(n res_users_apikeys "true")" "0"
check "secret parameters" "$(n ir_config_parameter "key ~ '(secret|token|client_id|api_key|password)' AND key <> 'database.secret'")" "0"
check "marked as anonymised" "$(q "SELECT coalesce((SELECT lower(value) FROM ir_config_parameter WHERE key = 'database.is_anonymized'), 'missing')")" "true"
if [ "$fail" -ne 0 ]; then
    echo "[fail] ${DB} still holds people's data: do not start the instance on it." >&2
    exit 1
fi

echo "--> local admin"
printf "env['res.users'].browse(2).write({'password': %s})\nenv.cr.commit()\n" "$(python3 -c 'import json,sys; print(json.dumps(sys.argv[1]))' "$ADMIN_PASSWORD")" \
    | docker compose -f "$COMPOSE" run --rm -T --no-deps --entrypoint /entrypoint.sh "$WEB" \
        odoo shell -c "$CONF" -d "$DB" --no-http --log-level=warn >/dev/null
echo "[ok] ${DB} anonymised and verified; login admin with the given password."
