with AmountsPerDate as (
    select
        visited_on
        , sum(amount) as amount
    from Customer
    group by visited_on
)
, MovingAmounts as (
    select
        visited_on
        , sum(amount) over (order by visited_on rows between 6 preceding and current row) as amount
        , round(avg(cast(amount as float)) over (order by visited_on rows between 6 preceding and current row), 2) as average_amount
    from AmountsPerDate
)
select
    *
from MovingAmounts
where datediff(day, (select min(visited_on) from MovingAmounts), visited_on) >= 6
order by visited_on
