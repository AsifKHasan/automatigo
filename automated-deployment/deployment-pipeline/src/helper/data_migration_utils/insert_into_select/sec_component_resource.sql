INSERT INTO sec.component_resource(oid, status, resource_oid, component_oid)
SELECT oid, status, resource_oid, component_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, status, resource_oid, component_oid
FROM sec.component_resource')
AS x(oid character varying, status character varying, resource_oid character varying, component_oid character varying);
