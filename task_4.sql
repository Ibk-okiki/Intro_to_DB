-- task_4.sql
-- Script to print full description of Books table from alx_book_store database
-- Using INFORMATION_SCHEMA to get table structure information

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';
