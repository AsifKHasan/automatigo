INSERT INTO hrm.deputation_info(oid, type_ingoing, type_outgoing, employee_oid, previous_ministry, deputed_ministry, previous_organization, deputed_organization, no_of_go, order_date, start_date, time_period)
SELECT oid, type_ingoing, type_outgoing, employee_oid, previous_ministry, deputed_ministry, previous_organization, deputed_organization, no_of_go, order_date, start_date, time_period
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, type_ingoing, type_outgoing, employee_oid, previous_ministry, deputed_ministry, previous_organization, deputed_organization, no_of_go, order_date, start_date, time_period
FROM hrm.deputation_info')
AS x(oid character varying, type_ingoing character varying, type_outgoing character varying, employee_oid character varying, previous_ministry character varying, deputed_ministry character varying, previous_organization character varying, deputed_organization character varying, no_of_go character varying, order_date timestamp without time zone, start_date timestamp without time zone, time_period numeric);
