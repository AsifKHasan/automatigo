INSERT INTO cmn.committee_setup(oid, committee_code, committee_type_oid, committee_name, max_member, min_member, forming_date, purpose, comments, status, organization_info_oid)
SELECT oid, committee_code, committee_type_oid, committee_name, max_member, min_member, forming_date, purpose, comments, status, organization_info_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, committee_code, committee_type_oid, committee_name, max_member, min_member, forming_date, purpose, comments, status, organization_info_oid
FROM cmn.committee_setup')
AS x(oid character varying, committee_code character varying, committee_type_oid character varying, committee_name character varying, max_member character varying, min_member character varying, forming_date date, purpose character varying, comments text, status character varying, organization_info_oid character varying);
