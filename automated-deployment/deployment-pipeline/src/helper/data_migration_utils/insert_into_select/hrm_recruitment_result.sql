INSERT INTO hrm.recruitment_result(oid, attachment_url, circular_oid, written_marks, viva_marks, applicant_oid)
SELECT oid, attachment_url, circular_oid, written_marks, viva_marks, applicant_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, attachment_url, circular_oid, written_marks, viva_marks, applicant_oid
FROM hrm.recruitment_result')
AS x(oid character varying, attachment_url character varying, circular_oid character varying, written_marks numeric, viva_marks numeric, applicant_oid character varying);
