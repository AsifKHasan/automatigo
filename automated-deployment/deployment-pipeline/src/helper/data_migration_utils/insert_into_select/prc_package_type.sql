INSERT INTO prc.package_type(oid, code, name_en, name_bn, description)
SELECT oid, code, name_en, name_bn, description
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, code, name_en, name_bn, description
FROM prc.package_type')
AS x(oid character varying, code character varying, name_en character varying, name_bn character varying, description text);
