INSERT INTO sec.office_module(oid, status, module_oid, office_oid, dashboard_url, service_url, zuul_url)
SELECT oid, status, module_oid, office_oid, dashboard_url, service_url, zuul_url
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, status, module_oid, office_oid, dashboard_url, service_url, zuul_url
FROM sec.office_module')
AS x(oid character varying, status character varying, module_oid character varying, office_oid character varying, dashboard_url character varying, service_url character varying, zuul_url character varying);
