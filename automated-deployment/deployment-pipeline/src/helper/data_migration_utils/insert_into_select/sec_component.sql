INSERT INTO sec.component(oid, name_en, name_bn, status, url, subfeature_oid)
SELECT oid, name_en, name_bn, status, url, subfeature_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, status, url, subfeature_oid
FROM sec.component')
AS x(oid character varying, name_en character varying, name_bn character varying, status character varying, url character varying, subfeature_oid character varying);
