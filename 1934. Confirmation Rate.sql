SELECT 
  Signups.user_id, 
  (
    ROUND(
      (
        CAST (
          COUNT(
            CASE WHEN action = 'confirmed' THEN action END
          ) AS DECIMAL(10, 2)
        ) / COUNT(*)
      ), 
      2
    )
  ) as confirmation_rate 
FROM 
  Signups 
  LEFT JOIN Confirmations on Signups.user_id = Confirmations.user_id 
GROUP BY 
  Signups.user_id
