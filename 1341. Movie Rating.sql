set nocount on;

create table #User(
    name varchar(30)
);

create table #Movie(
    title varchar(30)
);

with UsersWithMostRatings as (
    select top(1) with ties
        user_id
        , count(*) as num_movies_rated
    from MovieRating
    group by user_id
    order by num_movies_rated desc
)
insert #User
select top(1)
    Users.name
from UsersWithMostRatings
join Users
    on UsersWithMostRatings.user_id = Users.user_id
order by Users.name;

with MoviesWithHighestRatingFeb2010 as (
    select top(1) with ties
        movie_id
        , avg(cast(rating as float)) as avg_rating
    from MovieRating
    where
        year(created_at) = 2020
        and month(created_at) = 2 -- February
    group by movie_id
    order by avg_rating desc
)
insert #Movie
select top(1)
    Movies.title
from MoviesWithHighestRatingFeb2010
join Movies
    on MoviesWithHighestRatingFeb2010.movie_id = Movies.movie_id
order by Movies.title;

select
    name as results
from
    #User
union all -- in case user name and movie title are the same
select 
    title as results
from #Movie;

drop table #User;
drop table #Movie;
