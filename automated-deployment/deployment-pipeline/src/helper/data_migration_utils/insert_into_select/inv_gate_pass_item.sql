INSERT INTO inv.gate_pass_item(item_id, quantity, unit_id, gate_pass_id, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by)
SELECT item_id, quantity, unit_id, gate_pass_id, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT item_id, quantity, unit_id, gate_pass_id, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by
FROM inv.gate_pass_item')
AS x(item_id uuid, quantity numeric, unit_id uuid, gate_pass_id uuid, id uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid);
