-- create table with given specifications..
-- add restrictions to a column... (not null)
CREATE TABLE IF NOT EXISTS id_not_null(
id INT DEFAULT 1,
name VARCHAR(256)
);