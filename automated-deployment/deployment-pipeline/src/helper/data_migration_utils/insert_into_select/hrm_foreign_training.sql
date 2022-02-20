INSERT INTO hrm.foreign_training(oid, training_type_oid, training_title, institution, country, starting_from, end_to, sponsoring_agency)
SELECT oid, training_type_oid, training_title, institution, country, starting_from, end_to, sponsoring_agency
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, training_type_oid, training_title, institution, country, starting_from, end_to, sponsoring_agency
FROM hrm.foreign_training')
AS x(oid character varying, training_type_oid character varying, training_title character varying, institution character varying, country character varying, starting_from timestamp without time zone, end_to timestamp without time zone, sponsoring_agency character varying);
