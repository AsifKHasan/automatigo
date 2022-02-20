INSERT INTO hrm.investigation_under_controlling_auth(oid, employee_oid, date_of_submission, evaluation_by_ca, decision_status, application_code, decision_by, notes, esign)
SELECT oid, employee_oid, date_of_submission, evaluation_by_ca, decision_status, application_code, decision_by, notes, esign
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, date_of_submission, evaluation_by_ca, decision_status, application_code, decision_by, notes, esign
FROM hrm.investigation_under_controlling_auth')
AS x(oid character varying, employee_oid character varying, date_of_submission timestamp without time zone, evaluation_by_ca numeric, decision_status character varying, application_code character varying, decision_by character varying, notes text, esign character varying);
