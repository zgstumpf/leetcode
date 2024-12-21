select
      case
            when id % 2 != 0 and id != (select max(id) from Seat)
                then id + 1
            when id % 2 = 0 
                then id - 1
            else id -- if last id is odd, do nothing
      end as id
    , student
from Seat
order by id
