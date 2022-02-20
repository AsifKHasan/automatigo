INSERT INTO inv.material_delivery_detail_track(id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, received_qty, passed_qty, status, received_by, inspected_by, is_store_received, material_delivery_detail_id)
SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, received_qty, passed_qty, status, received_by, inspected_by, is_store_received, material_delivery_detail_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, received_qty, passed_qty, status, received_by, inspected_by, is_store_received, material_delivery_detail_id
FROM inv.material_delivery_detail_track')
AS x(id uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid, received_qty numeric, passed_qty numeric, status text, received_by uuid, inspected_by uuid, is_store_received boolean, material_delivery_detail_id uuid);
