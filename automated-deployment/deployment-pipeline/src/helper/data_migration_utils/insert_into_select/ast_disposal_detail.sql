INSERT INTO ast.disposal_detail(oid, code, expert_decision_oid, disposal_date, filepath, remarks, office_oid, created_by, created_on, updated_by, updated_on)
SELECT oid, code, expert_decision_oid, disposal_date, filepath, remarks, office_oid, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, code, expert_decision_oid, disposal_date, filepath, remarks, office_oid, created_by, created_on, updated_by, updated_on
FROM ast.disposal_detail')
AS x(oid character varying, code character varying, expert_decision_oid character varying, disposal_date date, filepath character varying, remarks text, office_oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
