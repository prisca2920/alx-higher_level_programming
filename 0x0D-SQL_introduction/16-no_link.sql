-- lists all records of 2nd table
-- in the mysql server
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
