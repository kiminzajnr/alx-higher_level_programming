-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- database name will be passed as argument of the mysql command
SELECT cities.id, name FROM cities WHERE state_id =
(SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
