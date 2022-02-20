INSERT INTO cmn.item_category(oid, name_en, name_bn, status, description, created_by, created_on, updated_by, updated_on, office_oid, is_deleted, parent_category_oid)
SELECT oid, name_en, name_bn, status, description, created_by, created_on, updated_by, updated_on, office_oid, is_deleted, parent_category_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, status, description, created_by, created_on, updated_by, updated_on, office_oid, is_deleted, parent_category_oid
FROM cmn.item_category')
AS x(oid character varying, name_en character varying, name_bn character varying, status character varying, description character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, office_oid character varying, is_deleted character varying, parent_category_oid character varying);
