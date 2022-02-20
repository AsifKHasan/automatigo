INSERT INTO hrm.penalty_committee_list(oid, attendance_committee_oid, committee_name)
SELECT oid, attendance_committee_oid, committee_name
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, attendance_committee_oid, committee_name
FROM hrm.penalty_committee_list')
AS x(oid character varying, attendance_committee_oid character varying, committee_name character varying);
