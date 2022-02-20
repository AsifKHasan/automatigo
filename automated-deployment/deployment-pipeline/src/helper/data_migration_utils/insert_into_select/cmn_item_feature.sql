INSERT INTO cmn.item_feature(oid, value_en, value_bn, item_oid, item_group_feature_mapping_oid, created_by, created_on, updated_by, updated_on, office_oid, is_deleted)
SELECT oid, value_en, value_bn, item_oid, item_group_feature_mapping_oid, created_by, created_on, updated_by, updated_on, office_oid, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, value_en, value_bn, item_oid, item_group_feature_mapping_oid, created_by, created_on, updated_by, updated_on, office_oid, is_deleted
FROM cmn.item_feature')
AS x(oid character varying, value_en character varying, value_bn character varying, item_oid character varying, item_group_feature_mapping_oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, office_oid character varying, is_deleted character varying);
