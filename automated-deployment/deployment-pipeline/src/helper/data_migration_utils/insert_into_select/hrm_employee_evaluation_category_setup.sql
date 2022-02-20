INSERT INTO hrm.employee_evaluation_category_setup(oid, acr_form_part_number, acr_form_part_title, acr_form_evaluation_category)
SELECT oid, acr_form_part_number, acr_form_part_title, acr_form_evaluation_category
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, acr_form_part_number, acr_form_part_title, acr_form_evaluation_category
FROM hrm.employee_evaluation_category_setup')
AS x(oid character varying, acr_form_part_number numeric, acr_form_part_title character varying, acr_form_evaluation_category character varying);
