INSERT INTO hrm.acr_under_counter_signing_auth(oid, employee_oid, submission_date_ca, total_marks_ca, submission_date_csa, total_marks_csa, acr_form_upload, comments, e_sign_of_auth)
SELECT oid, employee_oid, submission_date_ca, total_marks_ca, submission_date_csa, total_marks_csa, acr_form_upload, comments, e_sign_of_auth
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, submission_date_ca, total_marks_ca, submission_date_csa, total_marks_csa, acr_form_upload, comments, e_sign_of_auth
FROM hrm.acr_under_counter_signing_auth')
AS x(oid character varying, employee_oid character varying, submission_date_ca timestamp without time zone, total_marks_ca character varying, submission_date_csa numeric, total_marks_csa numeric, acr_form_upload character varying, comments text, e_sign_of_auth character varying);
