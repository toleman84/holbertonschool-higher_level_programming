-- script that lists all the cities of California that can be found in the database hbtn_0d_usa

SELECT cities.id, name
FROM hbtn_0d_usa.cities
WHERE cities.state_id = 1
ORDER BY id ASC;
