INSERT INTO prc.requisition_information(oid, requisition_date, remarks, status, created_by, created_on, updated_by, updated_on, requisition_declaration_oid, office_oid, requisition_for)
SELECT oid, requisition_date, remarks, status, created_by, created_on, updated_by, updated_on, requisition_declaration_oid, office_oid, requisition_for
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, requisition_date, remarks, status, created_by, created_on, updated_by, updated_on, requisition_declaration_oid, office_oid, requisition_for
FROM prc.requisition_information')
AS x(oid character varying, requisition_date date, remarks text, status character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, requisition_declaration_oid character varying, office_oid character varying, requisition_for character varying);
