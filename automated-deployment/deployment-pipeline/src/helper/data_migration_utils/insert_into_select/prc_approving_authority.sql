INSERT INTO prc.approving_authority(oid, code, name_en, name_bn)
SELECT oid, code, name_en, name_bn
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, code, name_en, name_bn
FROM prc.approving_authority')
AS x(oid character varying, code character varying, name_en character varying, name_bn character varying);
