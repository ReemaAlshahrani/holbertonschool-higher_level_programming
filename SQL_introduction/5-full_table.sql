-- Retrieves the full table definition (CREATE TABLE statement) 
-- from the system metadata without using restricted commands.
SELECT CREATE_TABLE, TABLE_NAME 
FROM information_schema.TABLES 
WHERE TABLE_NAME = 'first_table';
