INSERT INTO hrm.rules_of_award_publication(oid, rules_and_regulations, assigned_by, assigned_on)
SELECT oid, rules_and_regulations, assigned_by, assigned_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, rules_and_regulations, assigned_by, assigned_on
FROM hrm.rules_of_award_publication')
AS x(oid character varying, rules_and_regulations text, assigned_by character varying, assigned_on timestamp without time zone);
