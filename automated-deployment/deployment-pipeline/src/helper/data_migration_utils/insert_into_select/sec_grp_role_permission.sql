INSERT INTO sec.grp_role_permission(oid, component_oid, grp_role_oid)
SELECT oid, component_oid, grp_role_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, component_oid, grp_role_oid
FROM sec.grp_role_permission')
AS x(oid character varying, component_oid character varying, grp_role_oid character varying);
