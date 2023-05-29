# Write your MySQL query statement below
SELECT id,
    (CASE
        WHEN id = (SELECT id FROM Tree WHERE p_id IS NULL) THEN 'Root'
        WHEN id IN (SELECT DISTINCT p_id FROM Tree) AND p_id IN (SELECT id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END) AS type
FROM Tree;