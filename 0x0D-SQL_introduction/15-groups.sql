-- lists number of records with the same score in the table second_table
-- list sorted by number of records descending
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
