SELECT 
    machine_id, 
    ROUND(
        (
            (
                SUM(CASE WHEN activity_type = 'end' THEN timestamp END)
              - SUM(CASE WHEN activity_type = 'start' THEN timestamp END) 
            ) 
            / COUNT(DISTINCT process_id) 
        )
      , 3) as processing_time
FROM Activity
GROUP BY machine_id;
