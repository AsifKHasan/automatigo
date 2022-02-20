INSERT INTO hrm.recruitment_committee(oid, committee_oid, committee_name, short_description, member_oid, member_name_en, member_name_bn, designation_en, designation_bn, role)
SELECT oid, committee_oid, committee_name, short_description, member_oid, member_name_en, member_name_bn, designation_en, designation_bn, role
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, committee_oid, committee_name, short_description, member_oid, member_name_en, member_name_bn, designation_en, designation_bn, role
FROM hrm.recruitment_committee')
AS x(oid character varying, committee_oid character varying, committee_name character varying, short_description text, member_oid character varying, member_name_en character varying, member_name_bn character varying, designation_en character varying, designation_bn character varying, role character varying);
