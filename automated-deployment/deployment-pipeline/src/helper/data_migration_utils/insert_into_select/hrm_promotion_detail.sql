INSERT INTO hrm.promotion_detail(oid, employee_oid, date_of_promotion, rank_en, rank_bn, nature_of_promotion, pay_scale, no_of_go)
SELECT oid, employee_oid, date_of_promotion, rank_en, rank_bn, nature_of_promotion, pay_scale, no_of_go
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, date_of_promotion, rank_en, rank_bn, nature_of_promotion, pay_scale, no_of_go
FROM hrm.promotion_detail')
AS x(oid character varying, employee_oid character varying, date_of_promotion timestamp without time zone, rank_en character varying, rank_bn character varying, nature_of_promotion character varying, pay_scale character varying, no_of_go character varying);
