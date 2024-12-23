with DistinctCustomer as (
    select distinct
        customer_id
        , product_key
    from Customer
)
, NumUniqueProductsBoughtPerCustomerId as (
    select
        customer_id
        , count(*) as num_unique_products_bought
    from DistinctCustomer
    group by customer_id
)
select
    customer_id
from NumUniqueProductsBoughtPerCustomerId
where num_unique_products_bought = (select count(*) from Product)
