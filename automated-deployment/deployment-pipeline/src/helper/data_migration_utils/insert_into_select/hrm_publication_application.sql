INSERT INTO hrm.publication_application(oid, employee_oid, publication_title, attachments, date_of_publication, notes, decision_status, application_code, decision_by)
SELECT oid, employee_oid, publication_title, attachments, date_of_publication, notes, decision_status, application_code, decision_by
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, publication_title, attachments, date_of_publication, notes, decision_status, application_code, decision_by
FROM hrm.publication_application')
AS x(oid character varying, employee_oid character varying, publication_title character varying, attachments character varying, date_of_publication timestamp without time zone, notes text, decision_status character varying, application_code character varying, decision_by character varying);
