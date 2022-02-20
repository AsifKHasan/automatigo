INSERT INTO hrm.employee_publication(oid, employee_oid, publication_title, publication_type, date_of_publication, description, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, publication_title, publication_type, date_of_publication, description, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, publication_title, publication_type, date_of_publication, description, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employee_publication')
AS x(oid character varying, employee_oid character varying, publication_title character varying, publication_type character varying, date_of_publication timestamp without time zone, description text, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
