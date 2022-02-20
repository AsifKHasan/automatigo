INSERT INTO cmn.donor_info(oid, donor_code, donor_name, party_type_oid, address, contact_no, organization, description, status)
SELECT oid, donor_code, donor_name, party_type_oid, address, contact_no, organization, description, status
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, donor_code, donor_name, party_type_oid, address, contact_no, organization, description, status
FROM cmn.donor_info')
AS x(oid character varying, donor_code character varying, donor_name character varying, party_type_oid character varying, address character varying, contact_no character varying, organization character varying, description text, status character varying);
