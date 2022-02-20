INSERT INTO hrm.leave_condition(oid, table_name, column_name, arithmatic_relation, value_leave, leave_type_oid, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, table_name, column_name, arithmatic_relation, value_leave, leave_type_oid, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, table_name, column_name, arithmatic_relation, value_leave, leave_type_oid, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.leave_condition')
AS x(oid character varying, table_name character varying, column_name character varying, arithmatic_relation character varying, value_leave character varying, leave_type_oid character varying, initialized_on timestamp without time zone, valid_till timestamp without time zone, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
