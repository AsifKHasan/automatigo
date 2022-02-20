INSERT INTO sec.grp_user_role(oid, menu_json, default_status, grp_role_oid, grp_user_oid, grp_module_oid, office_oid, active_status, created_by, created_on, updated_by, updated_on)
SELECT oid, menu_json, default_status, grp_role_oid, grp_user_oid, grp_module_oid, office_oid, active_status, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, menu_json, default_status, grp_role_oid, grp_user_oid, grp_module_oid, office_oid, active_status, created_by, created_on, updated_by, updated_on
FROM sec.grp_user_role')
AS x(oid character varying, menu_json text, default_status character varying, grp_role_oid character varying, grp_user_oid character varying, grp_module_oid character varying, office_oid character varying, active_status character varying, created_by character varying, created_on date, updated_by character varying, updated_on date);
