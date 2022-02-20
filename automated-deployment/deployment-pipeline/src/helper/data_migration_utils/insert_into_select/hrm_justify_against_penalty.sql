INSERT INTO hrm.justify_against_penalty(oid, penalty_oid, employee_oid, justification, attachment_url)
SELECT oid, penalty_oid, employee_oid, justification, attachment_url
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, penalty_oid, employee_oid, justification, attachment_url
FROM hrm.justify_against_penalty')
AS x(oid character varying, penalty_oid character varying, employee_oid character varying, justification text, attachment_url character varying);
