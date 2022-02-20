INSERT INTO hrm.publication_setup(oid, publication_title, publication_code, description, department, notes)
SELECT oid, publication_title, publication_code, description, department, notes
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, publication_title, publication_code, description, department, notes
FROM hrm.publication_setup')
AS x(oid character varying, publication_title character varying, publication_code text, description character varying, department character varying, notes text);
