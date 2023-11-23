-- displays the top 3 cities with the highest temperatures during july and august.
SELECT city, AVG(value) As avg_temp FROM temperatures WHERE month IN(7,8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
