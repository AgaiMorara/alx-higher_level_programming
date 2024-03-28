-- creates the table unique_id
-- restrictor (unique) and default
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE,
VARCHAR(256)
);
