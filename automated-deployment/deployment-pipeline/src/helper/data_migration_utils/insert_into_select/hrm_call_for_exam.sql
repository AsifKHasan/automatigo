INSERT INTO hrm.call_for_exam(oid, circular_oid, exam_configuration_oid, exam_code, exam_date, exam_type, exam_start, exam_end)
SELECT oid, circular_oid, exam_configuration_oid, exam_code, exam_date, exam_type, exam_start, exam_end
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, circular_oid, exam_configuration_oid, exam_code, exam_date, exam_type, exam_start, exam_end
FROM hrm.call_for_exam')
AS x(oid character varying, circular_oid character varying, exam_configuration_oid character varying, exam_code character varying, exam_date timestamp without time zone, exam_type character varying, exam_start timestamp without time zone, exam_end timestamp without time zone);
