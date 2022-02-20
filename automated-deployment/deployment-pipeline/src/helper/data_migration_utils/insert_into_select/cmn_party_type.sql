INSERT INTO cmn.party_type(oid, party_type_code, party_type_name)
SELECT oid, party_type_code, party_type_name
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, party_type_code, party_type_name
FROM cmn.party_type')
AS x(oid character varying, party_type_code character varying, party_type_name character varying);
