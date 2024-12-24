select
    Manager.employee_id
    , Manager.name
    , count(Report.employee_id) as reports_count
    , round(
        avg(cast(Report.age as decimal(38, 35)))
      , 0) as average_age
from Employees as Manager
join Employees as Report
    on Manager.employee_id = Report.reports_to
group by Manager.employee_id, Manager.name
order by employee_id
