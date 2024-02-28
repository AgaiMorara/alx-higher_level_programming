-- creates the table force_name on mysql_server
-- Database name will be passed as argument

CRATE TABLE IF NOT EXISTS force_name {
      id INT,
      name VARCHAR(256) NOT NULL
      };
      
