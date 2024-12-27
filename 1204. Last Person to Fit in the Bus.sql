with QueueWithTotalWeight as (
    select
        *
        , sum(weight) over (order by turn) as total_weight
    from Queue
)
select top(1)
    person_name
from QueueWithTotalWeight
where total_weight <= 1000
order by total_weight desc
