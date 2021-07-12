-- displays all records of the second_table of database
-- result should display the score and the name, in descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
