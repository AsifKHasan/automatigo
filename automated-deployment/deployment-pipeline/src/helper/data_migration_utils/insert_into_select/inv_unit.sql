INSERT INTO inv.unit(unit_id, unit_name, unit_code, parent_unit_id, status, conversion_rate, owned_by, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id)
SELECT unit_id, unit_name, unit_code, parent_unit_id, status, conversion_rate, owned_by, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id
FROM dblink('dbname=grp_bcc_live',
'SELECT unit_id, unit_name, unit_code, parent_unit_id, status, conversion_rate, owned_by, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id
FROM inv.unit')
AS x(unit_id uuid, unit_name character varying, unit_code character varying, parent_unit_id uuid, status boolean, conversion_rate character varying, owned_by uuid, created_date timestamp without time zone, is_deleted boolean, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid);
