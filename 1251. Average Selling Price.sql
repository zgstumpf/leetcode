SELECT Prices.product_id,
       (ISNULL (ROUND ((CAST(SUM(price * ISNULL(units, 0)) AS decimal) / NULLIF(SUM(units), 0)), 2),
                0)) AS average_price
FROM Prices
LEFT JOIN UnitsSold ON 
    Prices.product_id = UnitsSold.product_id
    AND 
    purchase_date BETWEEN start_date AND end_date
GROUP BY Prices.product_id
