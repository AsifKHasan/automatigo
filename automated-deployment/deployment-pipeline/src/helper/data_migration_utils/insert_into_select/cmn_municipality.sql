INSERT INTO cmn.municipality(oid, name_en, name_bn, bbs_code, upazila_oid)
SELECT oid, name_en, name_bn, bbs_code, upazila_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, bbs_code, upazila_oid
FROM cmn.municipality')
AS x(oid character varying, name_en character varying, name_bn character varying, bbs_code character varying, upazila_oid character varying);
