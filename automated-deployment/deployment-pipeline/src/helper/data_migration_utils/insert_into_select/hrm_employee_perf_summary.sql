INSERT INTO hrm.employee_perf_summary(oid, unit_weight_of_perf_metrics, performance_metrics)
SELECT oid, unit_weight_of_perf_metrics, performance_metrics
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, unit_weight_of_perf_metrics, performance_metrics
FROM hrm.employee_perf_summary')
AS x(oid character varying, unit_weight_of_perf_metrics numeric, performance_metrics character varying);
