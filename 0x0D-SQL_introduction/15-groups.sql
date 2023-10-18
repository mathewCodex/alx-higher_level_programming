-- List the number of records with same score in the tables
-- Rec are ordered by decending count
SELECT 'score', COUNT(*) AS 'number'
FROM 'second_table'
GROUP BY 'score'
ORDER BY 'number' DESC;
