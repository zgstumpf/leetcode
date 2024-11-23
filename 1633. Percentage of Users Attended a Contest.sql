DECLARE @numUsers int = (SELECT COUNT(*) FROM Users);

SELECT 
    contest_id,
    ROUND(
        CAST(COUNT(user_id) AS decimal) / @numUsers * 100
    , 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id
