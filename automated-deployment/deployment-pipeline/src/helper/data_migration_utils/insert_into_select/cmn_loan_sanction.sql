INSERT INTO cmn.loan_sanction(oid, employee_oid, last_date_of_loan, date_of_retirement, loan_type, loan_amount, no_of_installment, loan_letter_upload, notes)
SELECT oid, employee_oid, last_date_of_loan, date_of_retirement, loan_type, loan_amount, no_of_installment, loan_letter_upload, notes
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, last_date_of_loan, date_of_retirement, loan_type, loan_amount, no_of_installment, loan_letter_upload, notes
FROM cmn.loan_sanction')
AS x(oid character varying, employee_oid character varying, last_date_of_loan date, date_of_retirement date, loan_type character varying, loan_amount numeric, no_of_installment numeric, loan_letter_upload character varying, notes text);
