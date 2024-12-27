with EmployeeWithNumDepartments as (
    select
        employee_id
        , department_id
        , primary_flag
        , count(department_id) over (partition by employee_id) as num_departments
    from Employee
)
select 
    employee_id
    , department_id
from EmployeeWithNumDepartments
where 
    (num_departments > 1 and primary_flag = 'Y')
    or num_departments = 1
