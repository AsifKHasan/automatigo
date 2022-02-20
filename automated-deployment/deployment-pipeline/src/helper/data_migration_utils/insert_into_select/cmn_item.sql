INSERT INTO cmn.item(oid, name_en, name_bn, item_code, item_status, item_group_oid, created_by, created_on, updated_by, updated_on, office_oid, is_deleted)
SELECT oid, name_en, name_bn, item_code, item_status, item_group_oid, created_by, created_on, updated_by, updated_on, office_oid, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, item_code, item_status, item_group_oid, created_by, created_on, updated_by, updated_on, office_oid, is_deleted
FROM cmn.item')
AS x(oid character varying, name_en character varying, name_bn character varying, item_code character varying, item_status character varying, item_group_oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, office_oid character varying, is_deleted character varying);
