# Write your MySQL query statement below
SELECT L.name AS Customers
FROM Customers L LEFT JOIN Orders R ON L.id = R.customerId
WHERE R.id IS NULL;