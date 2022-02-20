INSERT INTO prc.procurement_method(oid, name_en, name_bn, description)
SELECT oid, name_en, name_bn, description
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, description
FROM prc.procurement_method')
AS x(oid character varying, name_en character varying, name_bn character varying, description text);
