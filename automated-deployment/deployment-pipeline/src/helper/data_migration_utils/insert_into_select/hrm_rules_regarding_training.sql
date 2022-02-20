INSERT INTO hrm.rules_regarding_training(oid, training_type, rules_and_regulations, assigned_by, assigned_on)
SELECT oid, training_type, rules_and_regulations, assigned_by, assigned_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, training_type, rules_and_regulations, assigned_by, assigned_on
FROM hrm.rules_regarding_training')
AS x(oid character varying, training_type character varying, rules_and_regulations text, assigned_by character varying, assigned_on timestamp without time zone);
