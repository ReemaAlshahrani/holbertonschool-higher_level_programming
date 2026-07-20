-- Creates the table 'first_table' in the current database.
-- 'IF NOT EXISTS' prevents the script from failing if the table already exists.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
