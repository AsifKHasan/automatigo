INSERT INTO inv.reorder_level(reorderlevel_id, store_id, item_id, cat_id, unit_id, reorder_level, low_level, high_level, remarks, owned_by, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id)
SELECT reorderlevel_id, store_id, item_id, cat_id, unit_id, reorder_level, low_level, high_level, remarks, owned_by, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id
FROM dblink('dbname=grp_bcc_live',
'SELECT reorderlevel_id, store_id, item_id, cat_id, unit_id, reorder_level, low_level, high_level, remarks, owned_by, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id
FROM inv.reorder_level')
AS x(reorderlevel_id uuid, store_id uuid, item_id uuid, cat_id uuid, unit_id uuid, reorder_level numeric, low_level numeric, high_level numeric, remarks character varying, owned_by uuid, created_date timestamp without time zone, is_deleted boolean, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid);
