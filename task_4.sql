-- task_4.sql
-- Script to print full description of Books table from alx_book_store database
-- Using INFORMATION_SCHEMA to get table structure information

SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Books';
