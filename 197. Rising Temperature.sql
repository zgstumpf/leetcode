SELECT today.id
FROM Weather today
JOIN Weather yesterday 
ON DATEDIFF(today.recordDate, yesterday.recordDate) = 1
WHERE today.temperature > yesterday.temperature;
