-- a script that lists the number of records with the same score in the table
-- The result should display the score and number of same scores
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score
ORDER BY number DESC;
