INSERT INTO hrm.survey_questionnaire_for_trainer(oid, training_type_oid, trainer_detail_oid, question)
SELECT oid, training_type_oid, trainer_detail_oid, question
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, training_type_oid, trainer_detail_oid, question
FROM hrm.survey_questionnaire_for_trainer')
AS x(oid character varying, training_type_oid character varying, trainer_detail_oid character varying, question character varying);
