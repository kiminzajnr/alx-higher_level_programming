-- lists all records with a score >= 10 in table second_table
-- display both the score and the name, and database is passed as an argument of the mysql command
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
