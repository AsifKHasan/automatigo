INSERT INTO hrm.trainee_result(oid, trainer, trainee, training, result)
SELECT oid, trainer, trainee, training, result
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, trainer, trainee, training, result
FROM hrm.trainee_result')
AS x(oid character varying, trainer character varying, trainee character varying, training character varying, result character varying);
