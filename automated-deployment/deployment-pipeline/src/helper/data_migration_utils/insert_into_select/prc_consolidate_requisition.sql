INSERT INTO prc.consolidate_requisition(oid, status, created_by, created_on, updated_by, updated_on, office_oid, fiscal_year_oid, requisition_for, requisition_declaration_oid)
SELECT oid, status, created_by, created_on, updated_by, updated_on, office_oid, fiscal_year_oid, requisition_for, requisition_declaration_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, status, created_by, created_on, updated_by, updated_on, office_oid, fiscal_year_oid, requisition_for, requisition_declaration_oid
FROM prc.consolidate_requisition')
AS x(oid character varying, status character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, office_oid character varying, fiscal_year_oid character varying, requisition_for character varying, requisition_declaration_oid character varying);
