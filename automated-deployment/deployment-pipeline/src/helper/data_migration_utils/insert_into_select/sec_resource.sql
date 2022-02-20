INSERT INTO sec.resource(oid, end_point, status, service_oid)
SELECT oid, end_point, status, service_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, end_point, status, service_oid
FROM sec.resource')
AS x(oid character varying, end_point character varying, status character varying, service_oid character varying);
