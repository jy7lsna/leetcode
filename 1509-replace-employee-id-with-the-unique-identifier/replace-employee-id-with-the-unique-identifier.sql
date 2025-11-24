# Write your MySQL query statement below
SELECT emp.unique_id, e.name from Employees e
LEFT JOIN EmployeeUNI emp
ON e.id = emp.id