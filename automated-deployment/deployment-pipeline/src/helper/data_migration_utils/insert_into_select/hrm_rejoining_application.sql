INSERT INTO hrm.rejoining_application(oid, employee_leave_application_oid, rejoining_date, attachment_url, approver_oid, approval_date, approver_attachment_url, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_leave_application_oid, rejoining_date, attachment_url, approver_oid, approval_date, approver_attachment_url, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_leave_application_oid, rejoining_date, attachment_url, approver_oid, approval_date, approver_attachment_url, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.rejoining_application')
AS x(oid character varying, employee_leave_application_oid character varying, rejoining_date timestamp without time zone, attachment_url character varying, approver_oid character varying, approval_date timestamp without time zone, approver_attachment_url character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
