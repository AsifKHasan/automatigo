INSERT INTO cmn.deduction_setup(oid, grade, house_rent_deduction, tax_deduction, gpf_deduction, other_deduction, percentage, start_date, end_date)
SELECT oid, grade, house_rent_deduction, tax_deduction, gpf_deduction, other_deduction, percentage, start_date, end_date
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, grade, house_rent_deduction, tax_deduction, gpf_deduction, other_deduction, percentage, start_date, end_date
FROM cmn.deduction_setup')
AS x(oid character varying, grade character varying, house_rent_deduction numeric, tax_deduction numeric, gpf_deduction numeric, other_deduction numeric, percentage numeric, start_date date, end_date date);
