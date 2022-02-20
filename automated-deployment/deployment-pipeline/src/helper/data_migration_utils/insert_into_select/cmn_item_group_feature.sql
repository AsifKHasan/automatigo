INSERT INTO cmn.item_group_feature(oid, name_en, name_bn, created_by, created_on, updated_by, updated_on, office_oid, is_deleted)
SELECT oid, name_en, name_bn, created_by, created_on, updated_by, updated_on, office_oid, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, created_by, created_on, updated_by, updated_on, office_oid, is_deleted
FROM cmn.item_group_feature')
AS x(oid character varying, name_en character varying, name_bn character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, office_oid character varying, is_deleted character varying);
