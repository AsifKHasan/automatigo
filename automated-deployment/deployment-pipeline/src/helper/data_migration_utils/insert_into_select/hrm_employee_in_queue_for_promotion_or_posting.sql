INSERT INTO hrm.employee_in_queue_for_promotion_or_posting(oid, employee_oid, no_of_go)
SELECT oid, employee_oid, no_of_go
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, no_of_go
FROM hrm.employee_in_queue_for_promotion_or_posting')
AS x(oid character varying, employee_oid character varying, no_of_go character varying);
