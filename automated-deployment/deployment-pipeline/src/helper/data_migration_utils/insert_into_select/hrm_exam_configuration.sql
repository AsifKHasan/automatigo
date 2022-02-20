INSERT INTO hrm.exam_configuration(oid, exam_type, total_marks, pass_marks, assigned_by)
SELECT oid, exam_type, total_marks, pass_marks, assigned_by
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, exam_type, total_marks, pass_marks, assigned_by
FROM hrm.exam_configuration')
AS x(oid character varying, exam_type character varying, total_marks numeric, pass_marks numeric, assigned_by character varying);
