-- Query database to extract list of cities
-- given a restriction
SELECT id, name from cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;
