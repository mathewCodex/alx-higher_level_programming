--Lists all recs of the table second_table
--Records are ordered by DSC score
SELECT 'score', 'name'
FROM 'second_table'
WHERE 'name' != ""
ORDER BY 'SCORE' DESC
