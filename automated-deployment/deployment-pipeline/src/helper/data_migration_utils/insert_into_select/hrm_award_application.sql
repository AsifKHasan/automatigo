INSERT INTO hrm.award_application(oid, employee_oid, award_title, attachments, date_of_receiving_award, notes, decision_status, application_code, decision_by)
SELECT oid, employee_oid, award_title, attachments, date_of_receiving_award, notes, decision_status, application_code, decision_by
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, award_title, attachments, date_of_receiving_award, notes, decision_status, application_code, decision_by
FROM hrm.award_application')
AS x(oid character varying, employee_oid character varying, award_title character varying, attachments character varying, date_of_receiving_award timestamp without time zone, notes text, decision_status character varying, application_code character varying, decision_by character varying);
