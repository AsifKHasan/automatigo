INSERT INTO hrm.forbidden_pair(oid, first_leave_type_oid, second_leave_type_oid, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, first_leave_type_oid, second_leave_type_oid, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, first_leave_type_oid, second_leave_type_oid, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.forbidden_pair')
AS x(oid character varying, first_leave_type_oid character varying, second_leave_type_oid character varying, initialized_on timestamp without time zone, valid_till timestamp without time zone, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
