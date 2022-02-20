INSERT INTO hrm.organisational_training(oid, is_mandatory, duration, training_type_oid, objective, descriptions, training_name, start_date, end_date, start_time, end_time, organization, designation_required, education_required)
SELECT oid, is_mandatory, duration, training_type_oid, objective, descriptions, training_name, start_date, end_date, start_time, end_time, organization, designation_required, education_required
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, is_mandatory, duration, training_type_oid, objective, descriptions, training_name, start_date, end_date, start_time, end_time, organization, designation_required, education_required
FROM hrm.organisational_training')
AS x(oid character varying, is_mandatory character varying, duration numeric, training_type_oid character varying, objective text, descriptions text, training_name character varying, start_date timestamp without time zone, end_date timestamp without time zone, start_time timestamp without time zone, end_time timestamp without time zone, organization character varying, designation_required text, education_required text);
