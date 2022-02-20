INSERT INTO cmn.geo_post_office(oid, name_en, name_bn, bbs_code, union_oid)
SELECT oid, name_en, name_bn, bbs_code, union_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, bbs_code, union_oid
FROM cmn.geo_post_office')
AS x(oid character varying, name_en character varying, name_bn character varying, bbs_code character varying, union_oid character varying);
