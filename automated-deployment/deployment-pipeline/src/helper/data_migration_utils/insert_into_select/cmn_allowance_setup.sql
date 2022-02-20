INSERT INTO cmn.allowance_setup(oid, grade, house_rent_allowance, medical_allowance, mobile_allowance, other_allowance, percentage, start_date, end_date)
SELECT oid, grade, house_rent_allowance, medical_allowance, mobile_allowance, other_allowance, percentage, start_date, end_date
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, grade, house_rent_allowance, medical_allowance, mobile_allowance, other_allowance, percentage, start_date, end_date
FROM cmn.allowance_setup')
AS x(oid character varying, grade character varying, house_rent_allowance numeric, medical_allowance numeric, mobile_allowance numeric, other_allowance numeric, percentage numeric, start_date date, end_date date);
