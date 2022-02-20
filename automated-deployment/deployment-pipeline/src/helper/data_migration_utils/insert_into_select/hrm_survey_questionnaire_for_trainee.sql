INSERT INTO hrm.survey_questionnaire_for_trainee(oid, training_oid, question)
SELECT oid, training_oid, question
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, training_oid, question
FROM hrm.survey_questionnaire_for_trainee')
AS x(oid character varying, training_oid character varying, question character varying);
