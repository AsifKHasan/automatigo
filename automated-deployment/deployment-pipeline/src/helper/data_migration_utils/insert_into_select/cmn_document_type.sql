INSERT INTO cmn.document_type(oid, document_type_code, document_type_name)
SELECT oid, document_type_code, document_type_name
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, document_type_code, document_type_name
FROM cmn.document_type')
AS x(oid character varying, document_type_code character varying, document_type_name character varying);
