select
    product_id
    , year as first_year
    , quantity
    , price
from Sales main
where year = (
    select 
        min(year) 
    from Sales 
    where product_id = main.product_id)
