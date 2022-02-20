INSERT INTO hrm.apply_for_prl(oid, employee_oid, duration_from, duration_to, prl_duration, file_title, file_code, file_type, attachment, decision_status, application_code, decision_by)
SELECT oid, employee_oid, duration_from, duration_to, prl_duration, file_title, file_code, file_type, attachment, decision_status, application_code, decision_by
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, duration_from, duration_to, prl_duration, file_title, file_code, file_type, attachment, decision_status, application_code, decision_by
FROM hrm.apply_for_prl')
AS x(oid character varying, employee_oid character varying, duration_from timestamp without time zone, duration_to timestamp without time zone, prl_duration numeric, file_title character varying, file_code character varying, file_type character varying, attachment character varying, decision_status character varying, application_code character varying, decision_by character varying);
