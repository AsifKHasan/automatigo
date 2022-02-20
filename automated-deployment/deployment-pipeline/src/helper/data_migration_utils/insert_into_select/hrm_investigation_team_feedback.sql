INSERT INTO hrm.investigation_team_feedback(oid, employee_oid, date_of_submission, evaluation_by_investigation_team, notes, esign)
SELECT oid, employee_oid, date_of_submission, evaluation_by_investigation_team, notes, esign
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, date_of_submission, evaluation_by_investigation_team, notes, esign
FROM hrm.investigation_team_feedback')
AS x(oid character varying, employee_oid character varying, date_of_submission timestamp without time zone, evaluation_by_investigation_team numeric, notes text, esign character varying);
