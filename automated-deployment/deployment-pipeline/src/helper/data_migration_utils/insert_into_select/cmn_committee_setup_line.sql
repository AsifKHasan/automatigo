INSERT INTO cmn.committee_setup_line(oid, committee_setup_line_code, committee_setup_oid, employee_info_oid, member_role, orgaization_oid)
SELECT oid, committee_setup_line_code, committee_setup_oid, employee_info_oid, member_role, orgaization_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, committee_setup_line_code, committee_setup_oid, employee_info_oid, member_role, orgaization_oid
FROM cmn.committee_setup_line')
AS x(oid character varying, committee_setup_line_code character varying, committee_setup_oid character varying, employee_info_oid character varying, member_role character varying, orgaization_oid character varying);
