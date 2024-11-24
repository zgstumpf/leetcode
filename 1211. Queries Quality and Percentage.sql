SELECT
  query_name,
  ROUND(AVG(CAST(rating AS decimal) / position), 2) AS quality,
  ROUND(
    AVG(
      CAST(
        CASE
          WHEN rating < 3 THEN 1
          ELSE 0
        END AS decimal
      )
    ) * 100,
    2
  ) AS poor_query_percentage
FROM
  Queries
WHERE query_name IS NOT NULL
GROUP BY
  query_name
