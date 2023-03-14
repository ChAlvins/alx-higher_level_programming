-- Lists all records of the table second_table having a name value.
-- Don’t list rows without a name value
-- Results display the score and the name (in this order)
-- Records are ordered by descending score.
SELECT score, name FROM second_table
WHERE name != ""
ORDER BY score DESC
