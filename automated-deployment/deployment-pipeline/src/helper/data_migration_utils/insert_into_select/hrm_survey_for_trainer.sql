INSERT INTO hrm.survey_for_trainer(oid, training_type_oid, trainer_detail_oid, trainer_code, survey_question_code, answer)
SELECT oid, training_type_oid, trainer_detail_oid, trainer_code, survey_question_code, answer
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, training_type_oid, trainer_detail_oid, trainer_code, survey_question_code, answer
FROM hrm.survey_for_trainer')
AS x(oid character varying, training_type_oid character varying, trainer_detail_oid character varying, trainer_code character varying, survey_question_code character varying, answer character varying);
