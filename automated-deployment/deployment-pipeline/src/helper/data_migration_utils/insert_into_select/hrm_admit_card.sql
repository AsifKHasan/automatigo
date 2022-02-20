INSERT INTO hrm.admit_card(oid, exam_oid, applicant_oid, roll_no, exam_date, exam_venue, exam_type)
SELECT oid, exam_oid, applicant_oid, roll_no, exam_date, exam_venue, exam_type
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, exam_oid, applicant_oid, roll_no, exam_date, exam_venue, exam_type
FROM hrm.admit_card')
AS x(oid character varying, exam_oid character varying, applicant_oid character varying, roll_no numeric, exam_date timestamp without time zone, exam_venue character varying, exam_type character varying);
