INSERT INTO hrm.offense_setup(oid, offense_title, offense_code, description, start_date_of_offense, end_date_of_offense, go_number, esign)
SELECT oid, offense_title, offense_code, description, start_date_of_offense, end_date_of_offense, go_number, esign
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, offense_title, offense_code, description, start_date_of_offense, end_date_of_offense, go_number, esign
FROM hrm.offense_setup')
AS x(oid character varying, offense_title character varying, offense_code numeric, description text, start_date_of_offense timestamp without time zone, end_date_of_offense timestamp without time zone, go_number numeric, esign character varying);
