INSERT INTO hrm.pending_participation_confirmation(oid, training_oid, trainee_oid, is_attendant, reason)
SELECT oid, training_oid, trainee_oid, is_attendant, reason
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, training_oid, trainee_oid, is_attendant, reason
FROM hrm.pending_participation_confirmation')
AS x(oid character varying, training_oid character varying, trainee_oid character varying, is_attendant character varying, reason character varying);
