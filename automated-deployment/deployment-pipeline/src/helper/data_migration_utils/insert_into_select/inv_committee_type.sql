INSERT INTO inv.committee_type(ct_id, ct_name, ct_ref_no, status, created_date, is_deleted, owned_by, user_id, employee_id, proxy_user_id, org_id)
SELECT ct_id, ct_name, ct_ref_no, status, created_date, is_deleted, owned_by, user_id, employee_id, proxy_user_id, org_id
FROM dblink('dbname=grp_bcc_live',
'SELECT ct_id, ct_name, ct_ref_no, status, created_date, is_deleted, owned_by, user_id, employee_id, proxy_user_id, org_id
FROM inv.committee_type')
AS x(ct_id uuid, ct_name character varying, ct_ref_no character varying, status boolean, created_date timestamp without time zone, is_deleted boolean, owned_by uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid);
