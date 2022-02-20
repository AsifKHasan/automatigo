INSERT INTO hrm.employee_other_services(oid, employee_oid, employer_name_en, employer_name_bn, employer_address, type_of_service, position, service_from, service_till, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, employer_name_en, employer_name_bn, employer_address, type_of_service, position, service_from, service_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, employer_name_en, employer_name_bn, employer_address, type_of_service, position, service_from, service_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employee_other_services')
AS x(oid character varying, employee_oid character varying, employer_name_en character varying, employer_name_bn character varying, employer_address character varying, type_of_service character varying, position character varying, service_from timestamp without time zone, service_till timestamp without time zone, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
