INSERT INTO hrm.posting_and_promotion_committee_setup(oid, committee_name, short_description, member_oid, role)
SELECT oid, committee_name, short_description, member_oid, role
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, committee_name, short_description, member_oid, role
FROM hrm.posting_and_promotion_committee_setup')
AS x(oid character varying, committee_name character varying, short_description text, member_oid character varying, role character varying);
