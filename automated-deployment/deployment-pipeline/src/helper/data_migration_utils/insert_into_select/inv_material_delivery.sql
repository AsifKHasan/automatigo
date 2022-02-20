INSERT INTO inv.material_delivery(id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, courier_send_date, courier_receive_date, comment, courier_id, courier_ref_no, status)
SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, courier_send_date, courier_receive_date, comment, courier_id, courier_ref_no, status
FROM dblink('dbname=grp_bcc_live',
'SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, courier_send_date, courier_receive_date, comment, courier_id, courier_ref_no, status
FROM inv.material_delivery')
AS x(id uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid, courier_send_date timestamp without time zone, courier_receive_date timestamp without time zone, comment text, courier_id uuid, courier_ref_no text, status text);
