-- script that lists the number of records with the same score in the table second_table
-- of the database hbtn_0c_0 in MySQL server
SELECT COUNT(*) AS number
FROM second_table
WHERE score;
