SELECT Project.project_id AS project_id ,

        -- Why does CAST(... AS float) result in off by 0.01?
       ROUND(AVG(CAST(Employee.experience_years AS decimal(18, 4))) , 2) AS average_years
FROM Project
JOIN Employee ON Project.employee_id = Employee.employee_id
GROUP BY Project.project_id
ORDER BY Project.project_id
