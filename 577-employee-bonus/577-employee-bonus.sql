# Write your MySQL query statement below
SELECT L.name, R.bonus AS bonus
FROM Employee L LEFT JOIN Bonus R ON L.empId=R.empId
WHERE R.bonus < 1000 OR R.bonus IS NULL;
