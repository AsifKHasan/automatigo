INSERT INTO hrm.posting_info(oid, employee_oid, division, district, starting_from, end_to, last_posting, pay_scale, no_of_go)
SELECT oid, employee_oid, division, district, starting_from, end_to, last_posting, pay_scale, no_of_go
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, division, district, starting_from, end_to, last_posting, pay_scale, no_of_go
FROM hrm.posting_info')
AS x(oid character varying, employee_oid character varying, division character varying, district character varying, starting_from timestamp without time zone, end_to timestamp without time zone, last_posting timestamp without time zone, pay_scale numeric, no_of_go character varying);
