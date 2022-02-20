INSERT INTO prc.procurement_type(oid, name_en, name_bn, description)
SELECT oid, name_en, name_bn, description
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, description
FROM prc.procurement_type')
AS x(oid character varying, name_en character varying, name_bn character varying, description text);
