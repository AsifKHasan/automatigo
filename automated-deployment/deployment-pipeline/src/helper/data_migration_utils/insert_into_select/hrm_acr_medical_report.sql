INSERT INTO hrm.acr_medical_report(oid, employee_oid, height, weight, eye_power, blood_group, blood_pressure, medical_class_division, attachment, date, esign)
SELECT oid, employee_oid, height, weight, eye_power, blood_group, blood_pressure, medical_class_division, attachment, date, esign
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, height, weight, eye_power, blood_group, blood_pressure, medical_class_division, attachment, date, esign
FROM hrm.acr_medical_report')
AS x(oid character varying, employee_oid character varying, height numeric, weight numeric, eye_power numeric, blood_group character varying, blood_pressure character varying, medical_class_division character varying, attachment character varying, date timestamp without time zone, esign character varying);
