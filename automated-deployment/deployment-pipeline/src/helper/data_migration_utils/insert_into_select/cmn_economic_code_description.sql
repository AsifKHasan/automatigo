INSERT INTO cmn.economic_code_description(oid, name_en, name_bn, created_by, created_on, updated_by, updated_on)
SELECT oid, name_en, name_bn, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, created_by, created_on, updated_by, updated_on
FROM cmn.economic_code_description')
AS x(oid character varying, name_en text, name_bn text, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
