INSERT INTO hrm.acr_main_report(oid, employee_oid, moral, intellectual, materialistic, recommend_for_training, qualification_for_promotion, other_recommendation, esign, designation_en, designation_bn)
SELECT oid, employee_oid, moral, intellectual, materialistic, recommend_for_training, qualification_for_promotion, other_recommendation, esign, designation_en, designation_bn
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, moral, intellectual, materialistic, recommend_for_training, qualification_for_promotion, other_recommendation, esign, designation_en, designation_bn
FROM hrm.acr_main_report')
AS x(oid character varying, employee_oid character varying, moral numeric, intellectual numeric, materialistic numeric, recommend_for_training numeric, qualification_for_promotion numeric, other_recommendation character varying, esign character varying, designation_en character varying, designation_bn character varying);
