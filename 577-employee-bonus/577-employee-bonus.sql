# # Write your MySQL query statement below
# SELECT L.name, R.bonus AS bonus
# FROM Employee L LEFT JOIN Bonus R ON L.empId=R.empId
# WHERE R.bonus < 1000 OR R.bonus IS NULL;

SELECT L.name, R.bonus
FROM Employee L LEFT JOIN Bonus R USING (empId)
WHERE COALESCE(R.bonus, 0) < 1000;