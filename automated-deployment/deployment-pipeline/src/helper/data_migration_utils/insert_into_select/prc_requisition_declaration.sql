INSERT INTO prc.requisition_declaration(oid, start_date, end_date, status, description, is_extended, declared_by, office_oid, fiscal_year_oid, created_by, created_on, updated_by, updated_on)
SELECT oid, start_date, end_date, status, description, is_extended, declared_by, office_oid, fiscal_year_oid, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, start_date, end_date, status, description, is_extended, declared_by, office_oid, fiscal_year_oid, created_by, created_on, updated_by, updated_on
FROM prc.requisition_declaration')
AS x(oid character varying, start_date date, end_date date, status character varying, description text, is_extended character varying, declared_by character varying, office_oid character varying, fiscal_year_oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
