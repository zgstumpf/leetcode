-- Learn more: https://livebook.manning.com/book/sql-server-mvp-deep-dives/chapter-5/34
with DenseRanks as (
  select
      *
      , dense_rank() over (order by id) as dense_rank
  from Stadium
  where people >= 100 -- filter out records with too few people as early as possible.
),
DenseRanksMinusIds as (
  select
    *
    , (dense_rank - id) as dense_rank_minus_id
  from DenseRanks
),
NumConsecutiveIdsInIsland as (
  select
    *
    , count(*) over (partition by dense_rank_minus_id) as num_consecutive_ids_in_island
  from DenseRanksMinusIds
)
select 
  id
  , visit_date
  , people
from NumConsecutiveIdsInIsland
where
  num_consecutive_ids_in_island >= 3
order by visit_date
