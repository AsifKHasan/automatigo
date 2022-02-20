INSERT INTO hrm.acr_under_controlling_ministry(oid, employee_oid, submission_date, submission_date_ca, total_marks_ca, submission_date_csa, total_marks_csa, date_of_filled_up_form, e_sign_of_auth)
SELECT oid, employee_oid, submission_date, submission_date_ca, total_marks_ca, submission_date_csa, total_marks_csa, date_of_filled_up_form, e_sign_of_auth
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, submission_date, submission_date_ca, total_marks_ca, submission_date_csa, total_marks_csa, date_of_filled_up_form, e_sign_of_auth
FROM hrm.acr_under_controlling_ministry')
AS x(oid character varying, employee_oid character varying, submission_date timestamp without time zone, submission_date_ca timestamp without time zone, total_marks_ca numeric, submission_date_csa timestamp without time zone, total_marks_csa numeric, date_of_filled_up_form timestamp without time zone, e_sign_of_auth character varying);
