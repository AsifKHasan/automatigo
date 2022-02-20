INSERT INTO inv.physical_inventory_details(physical_inventory_id, item_id, uom_id, physical_qty, inventory_qty, approved_qty, comments, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, adjustment_qty)
SELECT physical_inventory_id, item_id, uom_id, physical_qty, inventory_qty, approved_qty, comments, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, adjustment_qty
FROM dblink('dbname=grp_bcc_live',
'SELECT physical_inventory_id, item_id, uom_id, physical_qty, inventory_qty, approved_qty, comments, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, adjustment_qty
FROM inv.physical_inventory_details')
AS x(physical_inventory_id uuid, item_id uuid, uom_id uuid, physical_qty numeric, inventory_qty numeric, approved_qty numeric, comments character varying, id uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid, adjustment_qty numeric);
