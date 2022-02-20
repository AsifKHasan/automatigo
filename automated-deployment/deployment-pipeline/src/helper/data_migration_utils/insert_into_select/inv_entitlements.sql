INSERT INTO inv.entitlements(id, org_id, post_id, entitlement_item_id, type_id, started_from, is_deleted, created_by, created_at, updated_at)
SELECT id, org_id, post_id, entitlement_item_id, type_id, started_from, is_deleted, created_by, created_at, updated_at
FROM dblink('dbname=grp_bcc_live',
'SELECT id, org_id, post_id, entitlement_item_id, type_id, started_from, is_deleted, created_by, created_at, updated_at
FROM inv.entitlements')
AS x(id uuid, org_id uuid, post_id uuid, entitlement_item_id uuid, type_id uuid, started_from timestamp without time zone, is_deleted boolean, created_by uuid, created_at timestamp without time zone, updated_at timestamp without time zone);
