-- lists the number of records with the same socre in the second_TABLE
-- the result should display the score , then number of records with this score with the label number
SELECT score, count(*) AS number FROM second_table GROUP BY  score ORDER BY number DESC;
