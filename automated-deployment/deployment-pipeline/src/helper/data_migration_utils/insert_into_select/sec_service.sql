INSERT INTO sec.service(oid, name_en, name_bn, status)
SELECT oid, name_en, name_bn, status
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, status
FROM sec.service')
AS x(oid character varying, name_en character varying, name_bn character varying, status character varying);
