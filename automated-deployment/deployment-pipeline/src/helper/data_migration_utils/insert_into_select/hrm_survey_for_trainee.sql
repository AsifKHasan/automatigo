INSERT INTO hrm.survey_for_trainee(oid, training_type_oid, trainer_detail_oid, trainee_id, survey_question_code, answer)
SELECT oid, training_type_oid, trainer_detail_oid, trainee_id, survey_question_code, answer
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, training_type_oid, trainer_detail_oid, trainee_id, survey_question_code, answer
FROM hrm.survey_for_trainee')
AS x(oid character varying, training_type_oid character varying, trainer_detail_oid character varying, trainee_id character varying, survey_question_code character varying, answer character varying);
