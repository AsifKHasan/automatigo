INSERT INTO hrm.employee_probation(oid, employee_oid, probation_from, probation_till, extended_probation_from, extended_probation_till, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, probation_from, probation_till, extended_probation_from, extended_probation_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, probation_from, probation_till, extended_probation_from, extended_probation_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employee_probation')
AS x(oid character varying, employee_oid character varying, probation_from timestamp without time zone, probation_till timestamp without time zone, extended_probation_from timestamp without time zone, extended_probation_till timestamp without time zone, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
