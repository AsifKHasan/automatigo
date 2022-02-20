INSERT INTO hrm.acr_under_controlling_auth(oid, employee_oid, submission_date_ca, subject_of_evaluation, marks_from_ca, total_marks_ca, acr_form_upload, e_sign_of_authority)
SELECT oid, employee_oid, submission_date_ca, subject_of_evaluation, marks_from_ca, total_marks_ca, acr_form_upload, e_sign_of_authority
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, submission_date_ca, subject_of_evaluation, marks_from_ca, total_marks_ca, acr_form_upload, e_sign_of_authority
FROM hrm.acr_under_controlling_auth')
AS x(oid character varying, employee_oid character varying, submission_date_ca timestamp without time zone, subject_of_evaluation character varying, marks_from_ca numeric, total_marks_ca numeric, acr_form_upload character varying, e_sign_of_authority character varying);
