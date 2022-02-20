INSERT INTO cmn.donee_info(oid, donee_code, donee_name, party_type_oid, address, contact_no, organization, description, status)
SELECT oid, donee_code, donee_name, party_type_oid, address, contact_no, organization, description, status
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, donee_code, donee_name, party_type_oid, address, contact_no, organization, description, status
FROM cmn.donee_info')
AS x(oid character varying, donee_code character varying, donee_name character varying, party_type_oid character varying, address character varying, contact_no character varying, organization character varying, description text, status character varying);
