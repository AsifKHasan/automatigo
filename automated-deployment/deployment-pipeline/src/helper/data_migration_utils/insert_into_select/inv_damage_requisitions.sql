INSERT INTO inv.damage_requisitions(id, store_id, applicant_organisation_id, applicant_employee_id, request_date, reference_number, remarks, review_status, is_executed, is_deleted, created_by, created_at, updated_at)
SELECT id, store_id, applicant_organisation_id, applicant_employee_id, request_date, reference_number, remarks, review_status, is_executed, is_deleted, created_by, created_at, updated_at
FROM dblink('dbname=grp_bcc_live',
'SELECT id, store_id, applicant_organisation_id, applicant_employee_id, request_date, reference_number, remarks, review_status, is_executed, is_deleted, created_by, created_at, updated_at
FROM inv.damage_requisitions')
AS x(id uuid, store_id uuid, applicant_organisation_id uuid, applicant_employee_id uuid, request_date timestamp without time zone, reference_number character varying, remarks character varying, review_status character varying, is_executed boolean, is_deleted boolean, created_by uuid, created_at timestamp without time zone, updated_at timestamp without time zone);
