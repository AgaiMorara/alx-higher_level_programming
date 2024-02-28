-- create a user
-- assign  SPECIFIC PASSW0RD USING IDENTIFIED BY
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY  'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
