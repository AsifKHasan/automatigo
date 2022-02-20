INSERT INTO cmn.document(oid, document_code, document_name, document_type_oid, category, path, description)
SELECT oid, document_code, document_name, document_type_oid, category, path, description
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, document_code, document_name, document_type_oid, category, path, description
FROM cmn.document')
AS x(oid character varying, document_code character varying, document_name character varying, document_type_oid character varying, category character varying, path character varying, description text);
