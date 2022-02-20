INSERT INTO inv.material_delivery_detail(id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, quantity, status, store_item_requisition_id, store_item_requisition_detail_id, material_delivery_id)
SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, quantity, status, store_item_requisition_id, store_item_requisition_detail_id, material_delivery_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, quantity, status, store_item_requisition_id, store_item_requisition_detail_id, material_delivery_id
FROM inv.material_delivery_detail')
AS x(id uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid, quantity numeric, status text, store_item_requisition_id uuid, store_item_requisition_detail_id uuid, material_delivery_id uuid);
