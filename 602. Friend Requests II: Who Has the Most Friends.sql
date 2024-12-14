with request_id_and_accepter_id_combined as (
    select
        requester_id as id
    from RequestAccepted
    
    union all
    
    select
        accepter_id as id
    from RequestAccepted
)
select top(1)
    id
    , count(*) as num -- number of friends
from request_id_and_accepter_id_combined
group by id
order by num desc
