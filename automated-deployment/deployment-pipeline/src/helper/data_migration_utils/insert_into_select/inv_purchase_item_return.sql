INSERT INTO inv.purchase_item_return(id, purchase_item_delivery_location_id, return_date, returned_quantity, uom_id, return_reason, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, created_by, org_id, last_modified_by)
SELECT id, purchase_item_delivery_location_id, return_date, returned_quantity, uom_id, return_reason, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, created_by, org_id, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT id, purchase_item_delivery_location_id, return_date, returned_quantity, uom_id, return_reason, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, created_by, org_id, last_modified_by
FROM inv.purchase_item_return')
AS x(id uuid, purchase_item_delivery_location_id uuid, return_date timestamp without time zone, returned_quantity numeric, uom_id uuid, return_reason character varying, is_deleted boolean, created_at timestamp without time zone, updated_at timestamp without time zone, user_id uuid, employee_id uuid, proxy_user_id uuid, created_by uuid, org_id uuid, last_modified_by uuid);
