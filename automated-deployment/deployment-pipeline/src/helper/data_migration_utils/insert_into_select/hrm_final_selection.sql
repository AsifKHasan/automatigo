INSERT INTO hrm.final_selection(oid, candidate_oid, police_verification_attachment_url, medical_verification_url, remarks)
SELECT oid, candidate_oid, police_verification_attachment_url, medical_verification_url, remarks
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, candidate_oid, police_verification_attachment_url, medical_verification_url, remarks
FROM hrm.final_selection')
AS x(oid character varying, candidate_oid character varying, police_verification_attachment_url character varying, medical_verification_url character varying, remarks character varying);
