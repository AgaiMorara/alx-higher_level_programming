-- lists all records with a score >= 10 in the second table of the hbtn_0c_0
-- order is staill maintainded
SELECT score, name FROM second_table WHERE  score >= 10 ORDER BY score DESC;
