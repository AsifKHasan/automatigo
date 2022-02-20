INSERT INTO cmn.geo_country(oid, name_en, name_bn)
SELECT oid, name_en, name_bn
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn
FROM cmn.geo_country')
AS x(oid character varying, name_en character varying, name_bn character varying);
