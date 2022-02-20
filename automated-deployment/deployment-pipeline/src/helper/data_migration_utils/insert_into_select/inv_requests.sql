INSERT INTO inv.requests(id, created_on, module_name, user_id, org_id, employee_id, proxy_user_id)
SELECT id, created_on, module_name, user_id, org_id, employee_id, proxy_user_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, created_on, module_name, user_id, org_id, employee_id, proxy_user_id
FROM inv.requests')
AS x(id uuid, created_on timestamp without time zone, module_name character varying, user_id uuid, org_id uuid, employee_id uuid, proxy_user_id uuid);
