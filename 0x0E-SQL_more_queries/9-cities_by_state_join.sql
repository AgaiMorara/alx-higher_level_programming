-- Query returns columns from two different tables
-- sort by cities.id, inner join
SELECT cities.id, cities.name, states.name from cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id;
