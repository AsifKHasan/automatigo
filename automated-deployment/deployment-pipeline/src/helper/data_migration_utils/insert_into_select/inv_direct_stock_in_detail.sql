INSERT INTO inv.direct_stock_in_detail(id, direct_stock_in_id, item_id, unit_id, currency_uom_id, quantity, approved_qty, item_approval, item_rate, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by)
SELECT id, direct_stock_in_id, item_id, unit_id, currency_uom_id, quantity, approved_qty, item_approval, item_rate, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT id, direct_stock_in_id, item_id, unit_id, currency_uom_id, quantity, approved_qty, item_approval, item_rate, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM inv.direct_stock_in_detail')
AS x(id uuid, direct_stock_in_id uuid, item_id uuid, unit_id uuid, currency_uom_id uuid, quantity numeric, approved_qty numeric, item_approval boolean, item_rate numeric, is_deleted boolean, created_at timestamp without time zone, updated_at timestamp without time zone, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_by uuid, last_modified_by uuid);
