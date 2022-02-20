INSERT INTO inv.store_employee(id, store_id, active_date, emp_id, store_designation_id, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by)
SELECT id, store_id, active_date, emp_id, store_designation_id, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT id, store_id, active_date, emp_id, store_designation_id, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM inv.store_employee')
AS x(id uuid, store_id uuid, active_date timestamp without time zone, emp_id uuid, store_designation_id uuid, is_deleted boolean, created_at timestamp without time zone, updated_at timestamp without time zone, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_by uuid, last_modified_by uuid);
