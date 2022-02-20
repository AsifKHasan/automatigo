INSERT INTO hrm.acr_summary(oid, employee_oid, date_of_submission, subject_of_evaluation, obtained_marks, total_obtained_marks, esign)
SELECT oid, employee_oid, date_of_submission, subject_of_evaluation, obtained_marks, total_obtained_marks, esign
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, date_of_submission, subject_of_evaluation, obtained_marks, total_obtained_marks, esign
FROM hrm.acr_summary')
AS x(oid character varying, employee_oid character varying, date_of_submission timestamp without time zone, subject_of_evaluation character varying, obtained_marks numeric, total_obtained_marks numeric, esign character varying);
