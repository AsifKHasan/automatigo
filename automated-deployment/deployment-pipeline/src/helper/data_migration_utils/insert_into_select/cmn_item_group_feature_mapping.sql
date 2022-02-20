INSERT INTO cmn.item_group_feature_mapping(oid, is_mandatory, item_group_oid, item_group_feature_oid, created_by, created_on, updated_by, updated_on, office_oid, is_deleted)
SELECT oid, is_mandatory, item_group_oid, item_group_feature_oid, created_by, created_on, updated_by, updated_on, office_oid, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, is_mandatory, item_group_oid, item_group_feature_oid, created_by, created_on, updated_by, updated_on, office_oid, is_deleted
FROM cmn.item_group_feature_mapping')
AS x(oid character varying, is_mandatory character varying, item_group_oid character varying, item_group_feature_oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, office_oid character varying, is_deleted character varying);
