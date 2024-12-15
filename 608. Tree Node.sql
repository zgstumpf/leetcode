select
    id
    , case
        when p_id is null then 'Root'
        when not(exists(select 1 from Tree children where children.p_id = Tree.id)) 
            then 'Leaf'
        else 'Inner'
      end as type
from Tree
