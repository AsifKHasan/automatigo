INSERT INTO hrm.termination(oid, employee_oid, employee_post_oid, date_of_termination, reason, remarks, go_code, goverment_order, decision_status, application_code, decision_by)
SELECT oid, employee_oid, employee_post_oid, date_of_termination, reason, remarks, go_code, goverment_order, decision_status, application_code, decision_by
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, employee_post_oid, date_of_termination, reason, remarks, go_code, goverment_order, decision_status, application_code, decision_by
FROM hrm.termination')
AS x(oid character varying, employee_oid character varying, employee_post_oid character varying, date_of_termination timestamp without time zone, reason character varying, remarks text, go_code character varying, goverment_order character varying, decision_status character varying, application_code character varying, decision_by character varying);
