INSERT INTO cmn.prepare_salary_bill(oid, grade, employee_type, employee_oid, attachment)
SELECT oid, grade, employee_type, employee_oid, attachment
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, grade, employee_type, employee_oid, attachment
FROM cmn.prepare_salary_bill')
AS x(oid character varying, grade character varying, employee_type character varying, employee_oid character varying, attachment character varying);
