-- lists all the cities
-- that can be found in db
SELECT cities FROM hbtn_0d_usa.states
WHERE name = California
ORDER BY cities.id ASC;
