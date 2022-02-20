INSERT INTO hrm.leave_type_reason(oid, leave_type_oid, reason_en, reason_bn, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, leave_type_oid, reason_en, reason_bn, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, leave_type_oid, reason_en, reason_bn, initialized_on, valid_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.leave_type_reason')
AS x(oid character varying, leave_type_oid character varying, reason_en character varying, reason_bn character varying, initialized_on timestamp without time zone, valid_till timestamp without time zone, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
