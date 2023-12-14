-- lists all the cities
-- that can be found in db
SELECT cities FROM states
WHERE name = California
ORDER BY cities.id ASC;
