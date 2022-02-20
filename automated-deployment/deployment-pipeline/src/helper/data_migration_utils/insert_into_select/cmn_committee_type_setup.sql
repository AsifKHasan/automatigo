INSERT INTO cmn.committee_type_setup(oid, committee_type_code, committee_type, approved_by)
SELECT oid, committee_type_code, committee_type, approved_by
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, committee_type_code, committee_type, approved_by
FROM cmn.committee_type_setup')
AS x(oid character varying, committee_type_code character varying, committee_type character varying, approved_by character varying);
