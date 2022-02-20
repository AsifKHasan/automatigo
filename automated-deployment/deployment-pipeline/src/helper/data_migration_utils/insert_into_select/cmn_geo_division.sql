INSERT INTO cmn.geo_division(oid, name_en, name_bn, bbs_code, country_oid)
SELECT oid, name_en, name_bn, bbs_code, country_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, bbs_code, country_oid
FROM cmn.geo_division')
AS x(oid character varying, name_en character varying, name_bn character varying, bbs_code character varying, country_oid character varying);
