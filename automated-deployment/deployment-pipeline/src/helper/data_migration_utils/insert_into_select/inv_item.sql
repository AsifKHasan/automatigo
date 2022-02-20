INSERT INTO inv.item(id, item_setup_id, item_code, expiry_date, serial_no, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by)
SELECT id, item_setup_id, item_code, expiry_date, serial_no, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT id, item_setup_id, item_code, expiry_date, serial_no, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by
FROM inv.item')
AS x(id uuid, item_setup_id uuid, item_code character varying, expiry_date timestamp without time zone, serial_no character varying, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid);
