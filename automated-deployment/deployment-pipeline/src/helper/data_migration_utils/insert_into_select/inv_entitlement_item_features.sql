INSERT INTO inv.entitlement_item_features(id, entitlement_item_id, item_setup_feature_id, value, is_deleted, created_by, created_at, updated_at)
SELECT id, entitlement_item_id, item_setup_feature_id, value, is_deleted, created_by, created_at, updated_at
FROM dblink('dbname=grp_bcc_live',
'SELECT id, entitlement_item_id, item_setup_feature_id, value, is_deleted, created_by, created_at, updated_at
FROM inv.entitlement_item_features')
AS x(id uuid, entitlement_item_id uuid, item_setup_feature_id uuid, value character varying, is_deleted boolean, created_by uuid, created_at timestamp without time zone, updated_at timestamp without time zone);
