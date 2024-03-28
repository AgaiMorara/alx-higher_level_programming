--script that creates the database hbnt_0d_usa and table cities
-- state id cant be null and must be a foreign key that references id
CREATE database if not exists hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE if not exists cities(
id INT AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES states(id)
);
