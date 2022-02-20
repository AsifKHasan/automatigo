INSERT INTO cmn.city_corporation(oid, name_en, name_bn, bbs_code, district_oid)
SELECT oid, name_en, name_bn, bbs_code, district_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, bbs_code, district_oid
FROM cmn.city_corporation')
AS x(oid character varying, name_en character varying, name_bn character varying, bbs_code character varying, district_oid character varying);
