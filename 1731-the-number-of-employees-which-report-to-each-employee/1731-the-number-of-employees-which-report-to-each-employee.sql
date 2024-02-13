# Write your MySQL query statement below
SELECT 
    manager.employee_id, 
    manager.name,
    COUNT(employee.employee_id) as reports_count,
    ROUND(AVG(employee.age)) as average_age
FROM Employees employee
INNER JOIN Employees manager ON employee.reports_to = manager.employee_id
GROUP BY 
    manager.employee_id, 
    manager.name
ORDER BY manager.employee_id;