INSERT INTO cmn.fiscal_year(oid, name_en, name_bn, status, start_date, end_date)
SELECT oid, name_en, name_bn, status, start_date, end_date
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, status, start_date, end_date
FROM cmn.fiscal_year')
AS x(oid character varying, name_en character varying, name_bn character varying, status character varying, start_date date, end_date date);
