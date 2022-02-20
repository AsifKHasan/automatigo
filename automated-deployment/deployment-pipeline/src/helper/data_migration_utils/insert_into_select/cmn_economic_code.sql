INSERT INTO cmn.economic_code(oid, name_en, name_bn, description_oid, created_by, created_on, updated_by, updated_on)
SELECT oid, name_en, name_bn, description_oid, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, description_oid, created_by, created_on, updated_by, updated_on
FROM cmn.economic_code')
AS x(oid character varying, name_en character varying, name_bn character varying, description_oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
