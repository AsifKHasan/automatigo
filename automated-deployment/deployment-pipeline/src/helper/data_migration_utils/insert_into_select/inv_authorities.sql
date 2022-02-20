INSERT INTO inv.authorities(id, name, endpoint, method, service)
SELECT id, name, endpoint, method, service
FROM dblink('dbname=grp_bcc_live',
'SELECT id, name, endpoint, method, service
FROM inv.authorities')
AS x(id integer, name character varying, endpoint character varying, method character varying, service character varying);
