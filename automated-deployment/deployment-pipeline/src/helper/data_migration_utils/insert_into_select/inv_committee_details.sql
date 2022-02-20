INSERT INTO inv.committee_details(qcd_id, committee_id, emp_id, emp_roles, comments, owned_by, created_date, is_deleted)
SELECT qcd_id, committee_id, emp_id, emp_roles, comments, owned_by, created_date, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT qcd_id, committee_id, emp_id, emp_roles, comments, owned_by, created_date, is_deleted
FROM inv.committee_details')
AS x(qcd_id uuid, committee_id uuid, emp_id uuid, emp_roles character varying, comments character varying, owned_by uuid, created_date timestamp without time zone, is_deleted boolean);
