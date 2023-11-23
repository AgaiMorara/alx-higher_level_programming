-- script that lists all records of the second_talbe of the hbtn_0c_0 database.
-- all rws have a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
