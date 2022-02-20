INSERT INTO inv.purchase_item_delivery_location(id, purchase_order_detail_id, party_id, store_id, deliverable_quantity, received_quantity, returned_quantity, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, created_by, org_id, last_modified_by)
SELECT id, purchase_order_detail_id, party_id, store_id, deliverable_quantity, received_quantity, returned_quantity, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, created_by, org_id, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT id, purchase_order_detail_id, party_id, store_id, deliverable_quantity, received_quantity, returned_quantity, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, created_by, org_id, last_modified_by
FROM inv.purchase_item_delivery_location')
AS x(id uuid, purchase_order_detail_id uuid, party_id uuid, store_id uuid, deliverable_quantity numeric, received_quantity numeric, returned_quantity numeric, is_deleted boolean, created_at timestamp without time zone, updated_at timestamp without time zone, user_id uuid, employee_id uuid, proxy_user_id uuid, created_by uuid, org_id uuid, last_modified_by uuid);
