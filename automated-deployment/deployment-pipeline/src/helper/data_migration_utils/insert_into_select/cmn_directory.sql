INSERT INTO cmn.directory(oid, created_by, created_on, updated_by, updated_on, row_status, location, permission_type, allocated_size, used_space)
SELECT oid, created_by, created_on, updated_by, updated_on, row_status, location, permission_type, allocated_size, used_space
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, row_status, location, permission_type, allocated_size, used_space
FROM cmn.directory')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, row_status character varying, location character varying, permission_type character varying, allocated_size numeric, used_space numeric);
