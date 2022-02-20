INSERT INTO inv.entitlement_items(id, item_setup_id, is_deleted, created_by, created_at, updated_at)
SELECT id, item_setup_id, is_deleted, created_by, created_at, updated_at
FROM dblink('dbname=grp_bcc_live',
'SELECT id, item_setup_id, is_deleted, created_by, created_at, updated_at
FROM inv.entitlement_items')
AS x(id uuid, item_setup_id uuid, is_deleted boolean, created_by uuid, created_at timestamp without time zone, updated_at timestamp without time zone);
