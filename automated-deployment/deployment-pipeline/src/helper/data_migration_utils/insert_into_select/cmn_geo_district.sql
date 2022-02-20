INSERT INTO cmn.geo_district(oid, name_en, name_bn, bbs_code, division_oid)
SELECT oid, name_en, name_bn, bbs_code, division_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, bbs_code, division_oid
FROM cmn.geo_district')
AS x(oid character varying, name_en character varying, name_bn character varying, bbs_code character varying, division_oid character varying);
