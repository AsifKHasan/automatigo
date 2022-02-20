INSERT INTO cmn.uom(oid, name_en, name_bn, category_oid, created_by, created_on, updated_by, updated_on, status)
SELECT oid, name_en, name_bn, category_oid, created_by, created_on, updated_by, updated_on, status
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, category_oid, created_by, created_on, updated_by, updated_on, status
FROM cmn.uom')
AS x(oid character varying, name_en character varying, name_bn character varying, category_oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, status character varying);
