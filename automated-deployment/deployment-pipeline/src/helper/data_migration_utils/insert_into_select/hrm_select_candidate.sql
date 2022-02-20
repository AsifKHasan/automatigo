INSERT INTO hrm.select_candidate(oid, applicant_oid, circular_oid, is_selected)
SELECT oid, applicant_oid, circular_oid, is_selected
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, applicant_oid, circular_oid, is_selected
FROM hrm.select_candidate')
AS x(oid character varying, applicant_oid character varying, circular_oid character varying, is_selected character varying);
