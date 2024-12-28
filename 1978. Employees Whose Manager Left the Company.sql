select
    employee_id
from Employees as Employee
where 
    salary < 30000
    and manager_id is not null
    and not(exists(select 1 from Employees as Manager where Manager.employee_id = Employee.manager_id))
order by employee_id
