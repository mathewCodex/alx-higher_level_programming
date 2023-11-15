-- List all recs inthe table second_table
-- Rec are ordered by DSC score
SELECT 'score', 'name'
FROM 'second_table'
WHERE 'score' >= 10
ORDER BY 'score' DESC;
