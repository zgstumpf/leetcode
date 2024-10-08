SELECT name, bonus
FROM Employee
LEFT JOIN Bonus ON Employee.empId = Bonus.empID
WHERE Bonus IS NULL OR Bonus < 1000;
