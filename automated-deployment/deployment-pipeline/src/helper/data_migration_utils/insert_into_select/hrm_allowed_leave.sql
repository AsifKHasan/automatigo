INSERT INTO hrm.allowed_leave(oid, leave_type_oid, leave_type_reason_oid, leave_period_amount, leave_period_unit, allowed_amount, allowed_unit, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, leave_type_oid, leave_type_reason_oid, leave_period_amount, leave_period_unit, allowed_amount, allowed_unit, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, leave_type_oid, leave_type_reason_oid, leave_period_amount, leave_period_unit, allowed_amount, allowed_unit, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.allowed_leave')
AS x(oid character varying, leave_type_oid character varying, leave_type_reason_oid character varying, leave_period_amount numeric, leave_period_unit character varying, allowed_amount numeric, allowed_unit character varying, initialized_on timestamp without time zone, valid_till timestamp without time zone, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
