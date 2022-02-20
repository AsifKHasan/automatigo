INSERT INTO inv.view_item_opening_stock(item_id, id, item_name, category_id, cat_name, unit_id, unit_name, store_id, store_name)
SELECT item_id, id, item_name, category_id, cat_name, unit_id, unit_name, store_id, store_name
FROM dblink('dbname=grp_bcc_live',
'SELECT item_id, id, item_name, category_id, cat_name, unit_id, unit_name, store_id, store_name
FROM inv.view_item_opening_stock')
AS x(item_id uuid, id uuid, item_name character varying, category_id uuid, cat_name character varying, unit_id uuid, unit_name character varying, store_id uuid, store_name character varying);
