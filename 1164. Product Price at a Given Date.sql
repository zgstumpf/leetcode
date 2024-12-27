with ProductsOnOrBefore_2019_08_16 as (
    select
        *
    from Products
    where change_date <= '2019-08-16'
)
, ProductsRankedByMostRecentChange as (
    select
        *
        , row_number() over (partition by product_id order by change_date desc) as recent_order
    from ProductsOnOrBefore_2019_08_16
)
select
    product_id
    , new_price as price
from ProductsRankedByMostRecentChange
where recent_order = 1
union
select
    product_id
    , 10
from Products as ProductsWithoutChange
where not(exists(select product_id from ProductsOnOrBefore_2019_08_16 where product_id = ProductsWithoutChange.product_id))
