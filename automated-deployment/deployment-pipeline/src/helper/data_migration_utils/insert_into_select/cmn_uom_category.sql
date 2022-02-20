INSERT INTO cmn.uom_category(oid, name_en, name_bn, created_by, created_on, updated_by, updated_on, status)
SELECT oid, name_en, name_bn, created_by, created_on, updated_by, updated_on, status
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, created_by, created_on, updated_by, updated_on, status
FROM cmn.uom_category')
AS x(oid character varying, name_en character varying, name_bn character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, status character varying);
