INSERT INTO hrm.employee_education_qualification(oid, employee_oid, degree_title, institution_name, principal_subject, gpa_or_cgpa, year_of_passing, distinction, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, degree_title, institution_name, principal_subject, gpa_or_cgpa, year_of_passing, distinction, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, degree_title, institution_name, principal_subject, gpa_or_cgpa, year_of_passing, distinction, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employee_education_qualification')
AS x(oid character varying, employee_oid character varying, degree_title character varying, institution_name character varying, principal_subject character varying, gpa_or_cgpa character varying, year_of_passing numeric, distinction character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
