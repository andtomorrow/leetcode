SELECT R.name AS Department, L.name AS Employee, L.salary AS Salary
FROM Employee L, Department R
WHERE L.departmentId = R.id
    AND (R.name, L.salary) IN (SELECT R.name, max(L.salary) FROM  Employee L, Department R WHERE L.departmentId = R.id GROUP BY R.id);