INSERT INTO hrm.exam_venue(oid, applicant_oid, shortlist_oid, district, venue, exam_oid)
SELECT oid, applicant_oid, shortlist_oid, district, venue, exam_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, applicant_oid, shortlist_oid, district, venue, exam_oid
FROM hrm.exam_venue')
AS x(oid character varying, applicant_oid character varying, shortlist_oid character varying, district character varying, venue character varying, exam_oid character varying);
