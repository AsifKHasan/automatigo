INSERT INTO hrm.trainer_detail(oid, trainer_oid, training_history)
SELECT oid, trainer_oid, training_history
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, trainer_oid, training_history
FROM hrm.trainer_detail')
AS x(oid character varying, trainer_oid character varying, training_history character varying);
