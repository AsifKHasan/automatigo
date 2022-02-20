INSERT INTO hrm.investigation_team_setup(oid, committee_oid, employee_oid, controlling_authority, appointing_authority, assign_investigator, esign)
SELECT oid, committee_oid, employee_oid, controlling_authority, appointing_authority, assign_investigator, esign
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, committee_oid, employee_oid, controlling_authority, appointing_authority, assign_investigator, esign
FROM hrm.investigation_team_setup')
AS x(oid character varying, committee_oid character varying, employee_oid character varying, controlling_authority character varying, appointing_authority character varying, assign_investigator character varying, esign character varying);
