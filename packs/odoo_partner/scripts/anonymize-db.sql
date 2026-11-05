-- anonymize-db.sql — remove people's data and secrets from a neutralised copy of an Odoo Community database.
-- Run it through anonymize-db.sh (which neutralises first and verifies after), never on production.
-- Generic for Odoo 17-19 Community: every step checks that its table and columns exist, and a failing step is
-- reported as a NOTICE without stopping the others. What stays: the organisation's companies, configuration,
-- products, events (public), amounts and structure of invoices, memberships and orders.

CREATE OR REPLACE FUNCTION pg_temp.has_table(t text) RETURNS boolean LANGUAGE sql AS
$$ SELECT to_regclass('public.' || t) IS NOT NULL $$;

CREATE OR REPLACE FUNCTION pg_temp.has_col(t text, c text) RETURNS boolean LANGUAGE sql AS
$$ SELECT EXISTS (SELECT 1 FROM information_schema.columns
                  WHERE table_schema = 'public' AND table_name = t AND column_name = c) $$;

-- Run one statement if its table exists; on error, say so and go on.
CREATE OR REPLACE FUNCTION pg_temp.step(label text, t text, stmt text) RETURNS void LANGUAGE plpgsql AS $$
BEGIN
    IF NOT pg_temp.has_table(t) THEN
        RETURN;
    END IF;
    EXECUTE stmt;
    RAISE NOTICE 'ok: %', label;
EXCEPTION WHEN others THEN
    RAISE NOTICE 'FAILED: % (%)', label, SQLERRM;
END $$;

-- Set to NULL the listed columns of a table that exist and are nullable.
CREATE OR REPLACE FUNCTION pg_temp.null_cols(t text, cols text[], cond text DEFAULT 'true') RETURNS void
LANGUAGE plpgsql AS $$
DECLARE
    sets text;
BEGIN
    IF NOT pg_temp.has_table(t) THEN
        RETURN;
    END IF;
    SELECT string_agg(format('%I = NULL', column_name), ', ') INTO sets
      FROM information_schema.columns
     WHERE table_schema = 'public' AND table_name = t AND column_name = ANY (cols) AND is_nullable = 'YES';
    IF sets IS NOT NULL THEN
        PERFORM pg_temp.step(t || ': ' || array_to_string(cols, ','), t,
                             format('UPDATE %I SET %s WHERE %s', t, sets, cond));
    END IF;
END $$;

-- Same, for every column whose name matches a pattern (tokens, secrets, passwords).
CREATE OR REPLACE FUNCTION pg_temp.null_like(t text, pattern text) RETURNS void LANGUAGE plpgsql AS $$
DECLARE
    cols text[];
BEGIN
    SELECT array_agg(column_name::text) INTO cols
      FROM information_schema.columns
     WHERE table_schema = 'public' AND table_name = t AND column_name ~ pattern AND is_nullable = 'YES';
    IF cols IS NOT NULL THEN
        PERFORM pg_temp.null_cols(t, cols);
    END IF;
END $$;

-- Partners to keep as they are: the companies of the database and Odoo's technical partners.
CREATE TEMP TABLE keep_partner AS
    SELECT partner_id AS id FROM res_company
    UNION SELECT res_id FROM ir_model_data
           WHERE model = 'res.partner' AND module = 'base' AND name IN ('partner_root', 'public_partner');

-- People and organisations in the address book
SELECT pg_temp.step('res_partner: names, emails, addresses', 'res_partner', $s$
    UPDATE res_partner p SET
        name = CASE WHEN p.is_company THEN 'Organizzazione ' || p.id ELSE 'Persona ' || p.id END,
        email = 'contatto' || p.id || '@example.invalid',
        street = CASE WHEN p.street IS NULL THEN NULL ELSE 'Via Esempio ' || p.id END,
        zip = CASE WHEN p.zip IS NULL THEN NULL ELSE '00000' END
    WHERE p.id NOT IN (SELECT id FROM keep_partner) $s$);
SELECT pg_temp.step('res_partner: complete_name', 'res_partner',
    'UPDATE res_partner SET complete_name = name WHERE id NOT IN (SELECT id FROM keep_partner)')
 WHERE pg_temp.has_col('res_partner', 'complete_name');
SELECT pg_temp.step('res_partner: email_normalized', 'res_partner',
    'UPDATE res_partner SET email_normalized = email WHERE id NOT IN (SELECT id FROM keep_partner)')
 WHERE pg_temp.has_col('res_partner', 'email_normalized');
SELECT pg_temp.null_cols('res_partner',
    ARRAY['phone', 'mobile', 'phone_sanitized', 'street2', 'vat', 'comment', 'website', 'ref', 'function',
          'barcode', 'l10n_it_codice_fiscale', 'l10n_it_pec_email', 'l10n_it_pa_index', 'birthdate_date',
          'birthdate', 'gender', 'signup_token', 'signup_type', 'signup_expiration', 'company_registry',
          'peppol_endpoint', 'additional_info'],
    'id NOT IN (SELECT id FROM keep_partner)');
SELECT pg_temp.step('res_partner_bank', 'res_partner_bank',
    $s$UPDATE res_partner_bank SET acc_number = 'IT00X' || id, sanitized_acc_number = 'IT00X' || id$s$);
SELECT pg_temp.null_cols('res_partner_bank', ARRAY['acc_holder_name']);

-- Users: logins, signatures, second factors, keys, connected accounts
SELECT pg_temp.step('res_users: logins', 'res_users', $s$
    UPDATE res_users SET login = CASE WHEN id = 2 THEN 'admin' ELSE 'utente' || id || '@example.invalid' END $s$);
SELECT pg_temp.null_cols('res_users', ARRAY['signature', 'totp_secret', 'oauth_access_token', 'oauth_uid']);
SELECT pg_temp.step('res_users_apikeys', 'res_users_apikeys', 'DELETE FROM res_users_apikeys');
SELECT pg_temp.step('auth_passkey_key', 'auth_passkey_key', 'DELETE FROM auth_passkey_key');
SELECT pg_temp.step('auth_totp_device', 'auth_totp_device', 'DELETE FROM auth_totp_device');
SELECT pg_temp.null_like('res_users_settings', '(token|rtoken|sync)');
SELECT pg_temp.null_like('ir_mail_server', '(pass|token|secret)');
SELECT pg_temp.null_like('fetchmail_server', '(pass|token|secret)');
SELECT pg_temp.null_like('payment_provider', '(secret|api_key|_pass|password|private|_key$)');

-- Secrets and identity of the database
SELECT pg_temp.step('ir_config_parameter: secrets', 'ir_config_parameter', $s$
    DELETE FROM ir_config_parameter
     WHERE key ~ '(secret|token|client_id|_key$|api_key|password)' AND key <> 'database.secret' $s$);
SELECT pg_temp.step('ir_config_parameter: new database.secret and uuid', 'ir_config_parameter', $s$
    UPDATE ir_config_parameter SET value = CASE key
        WHEN 'database.secret' THEN md5(random()::text) || md5(random()::text)
        WHEN 'database.uuid' THEN gen_random_uuid()::text
        ELSE value END
     WHERE key IN ('database.secret', 'database.uuid') $s$);
SELECT pg_temp.step('iap_account', 'iap_account', 'DELETE FROM iap_account');
SELECT pg_temp.step('account_edi_proxy_client_user', 'account_edi_proxy_client_user',
    'DELETE FROM account_edi_proxy_client_user');
SELECT pg_temp.step('certificate_certificate', 'certificate_certificate', 'DELETE FROM certificate_certificate');
SELECT pg_temp.step('certificate_key', 'certificate_key', 'DELETE FROM certificate_key');
SELECT pg_temp.step('db_backup_configure', 'db_backup_configure', 'DELETE FROM db_backup_configure');

-- Messages, activities, notifications, traces
SELECT pg_temp.step('mail_message', 'mail_message', 'DELETE FROM mail_message');
SELECT pg_temp.step('mail_mail', 'mail_mail', 'DELETE FROM mail_mail');
SELECT pg_temp.step('mail_activity', 'mail_activity', 'DELETE FROM mail_activity');
SELECT pg_temp.step('mail_blacklist', 'mail_blacklist', 'DELETE FROM mail_blacklist');
SELECT pg_temp.step('phone_blacklist', 'phone_blacklist', 'DELETE FROM phone_blacklist');
SELECT pg_temp.step('sms_sms', 'sms_sms', 'DELETE FROM sms_sms');
SELECT pg_temp.step('snailmail_letter', 'snailmail_letter', 'DELETE FROM snailmail_letter');
SELECT pg_temp.step('website_visitor', 'website_visitor', 'DELETE FROM website_visitor');
SELECT pg_temp.step('privacy_log', 'privacy_log', 'DELETE FROM privacy_log');
SELECT pg_temp.null_cols('rating_rating', ARRAY['feedback']);

-- Documents: every stored file (invoices, IDs, photos...); Odoo rebuilds its web assets on its own
SELECT pg_temp.step('ir_attachment: stored files', 'ir_attachment',
    'DELETE FROM ir_attachment WHERE store_fname IS NOT NULL OR db_datas IS NOT NULL');

-- Business records: keep amounts and structure, drop what names or describes people
SELECT pg_temp.step('event_registration', 'event_registration', $s$
    UPDATE event_registration SET name = 'Partecipante ' || id,
        email = CASE WHEN email IS NULL THEN NULL ELSE 'iscrizione' || id || '@example.invalid' END $s$);
SELECT pg_temp.null_cols('event_registration', ARRAY['phone', 'mobile', 'company_name']);
SELECT pg_temp.step('event_registration_answer', 'event_registration_answer',
    $s$UPDATE event_registration_answer SET value_text_box = 'Risposta rimossa' WHERE value_text_box IS NOT NULL$s$);
SELECT pg_temp.step('calendar_event: names', 'calendar_event', $s$
    UPDATE calendar_event c SET name = 'Appuntamento ' || c.id
     WHERE NOT EXISTS (SELECT 1 FROM event_event e
                        WHERE position(to_jsonb(c.name::text)::text IN e.name::text) > 0) $s$)  -- name may be jsonb (translated)
 WHERE pg_temp.has_table('event_event');
SELECT pg_temp.null_cols('calendar_event', ARRAY['description', 'location', 'videocall_location']);
SELECT pg_temp.null_cols('calendar_attendee', ARRAY['common_name']);
SELECT pg_temp.step('account_move: partner name', 'account_move',
    $s$UPDATE account_move SET invoice_partner_display_name = 'Contatto ' || partner_id WHERE partner_id IS NOT NULL$s$)
 WHERE pg_temp.has_col('account_move', 'invoice_partner_display_name');
SELECT pg_temp.null_cols('account_move', ARRAY['narration']);
SELECT pg_temp.null_cols('account_bank_statement_line', ARRAY['partner_name', 'account_number']);
SELECT pg_temp.null_cols('sale_order', ARRAY['note', 'client_order_ref']);
SELECT pg_temp.step('project_task', 'project_task', $s$UPDATE project_task SET name = 'Attività ' || id$s$);
SELECT pg_temp.null_cols('project_task', ARRAY['description']);
SELECT pg_temp.step('crm_lead', 'crm_lead', $s$
    UPDATE crm_lead SET name = 'Opportunità ' || id,
        email_from = CASE WHEN email_from IS NULL THEN NULL ELSE 'lead' || id || '@example.invalid' END $s$);
SELECT pg_temp.null_cols('crm_lead', ARRAY['contact_name', 'partner_name', 'phone', 'mobile', 'description',
                                           'street', 'street2', 'city', 'zip', 'website', 'function']);
SELECT pg_temp.step('document_page', 'document_page',
    $s$UPDATE document_page SET content = '<p>Contenuto rimosso nella copia locale.</p>'$s$)
 WHERE pg_temp.has_col('document_page', 'content');
SELECT pg_temp.step('document_page_history', 'document_page_history', 'DELETE FROM document_page_history');

-- Links and tokens that would open records from outside
DO $$
DECLARE
    r record;
BEGIN
    FOR r IN SELECT table_name FROM information_schema.columns
              WHERE table_schema = 'public' AND column_name = 'access_token' AND is_nullable = 'YES'
                AND table_name IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public')
    LOOP
        PERFORM pg_temp.step(r.table_name || ': access_token', r.table_name,
                             format('UPDATE %I SET access_token = NULL', r.table_name));
    END LOOP;
END $$;

-- Local addresses
SELECT pg_temp.step('ir_config_parameter: web.base.url', 'ir_config_parameter',
    $s$UPDATE ir_config_parameter SET value = 'http://localhost:8069' WHERE key = 'web.base.url'$s$);
SELECT pg_temp.step('ir_config_parameter: mark anonymised', 'ir_config_parameter', $s$
    INSERT INTO ir_config_parameter (key, value, create_uid, write_uid, create_date, write_date)
    VALUES ('database.is_anonymized', 'True', 1, 1, now(), now())
    ON CONFLICT (key) DO UPDATE SET value = 'True' $s$);
