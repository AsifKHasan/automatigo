INSERT INTO inv.gate_pass(gate_pass_ref, officer_id, gate_pass_date, store_id, employee_name, remarks, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by)
SELECT gate_pass_ref, officer_id, gate_pass_date, store_id, employee_name, remarks, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT gate_pass_ref, officer_id, gate_pass_date, store_id, employee_name, remarks, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by
FROM inv.gate_pass')
AS x(gate_pass_ref character varying, officer_id uuid, gate_pass_date date, store_id uuid, employee_name character varying, remarks character varying, id uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid);
