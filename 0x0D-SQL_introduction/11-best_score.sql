-- lists all records with a score >= 10
SELECT score, name
FROM second_table
where score >= 10
ORDER BY score DESC
