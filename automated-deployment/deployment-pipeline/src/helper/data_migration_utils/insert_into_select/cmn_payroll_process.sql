INSERT INTO cmn.payroll_process(oid, employee_oid, house_rent, total_allowance, total_deduction, final_amount)
SELECT oid, employee_oid, house_rent, total_allowance, total_deduction, final_amount
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, house_rent, total_allowance, total_deduction, final_amount
FROM cmn.payroll_process')
AS x(oid character varying, employee_oid character varying, house_rent numeric, total_allowance numeric, total_deduction numeric, final_amount numeric);
