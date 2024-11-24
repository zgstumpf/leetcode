SELECT
  ROUND(AVG(CAST(immediate AS decimal)) * 100, 2) AS immediate_percentage
FROM
  (
    SELECT
      Delivery.customer_id,
      order_date,
      customer_pref_delivery_date,
      CASE
        WHEN order_date = customer_pref_delivery_date THEN 1
        ELSE 0
      END AS immediate
    FROM
      Delivery
      JOIN (
        SELECT
          customer_id,
          MIN(order_date) AS first_order_date
        FROM
          Delivery
        GROUP BY
          customer_id
      ) AS first_orders ON Delivery.customer_id = first_orders.customer_id
      AND Delivery.order_date = first_orders.first_order_date
  ) AS first_orders_with_immediate_marker
