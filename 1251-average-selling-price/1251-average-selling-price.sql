# Write your MySQL query statement below

SELECT L.product_id, ROUND(SUM(L.units*R.price)/SUM(L.units), 2) AS average_price
FROM UnitsSold L, Prices R
WHERE L.product_id = R.product_id AND
    (L.purchase_date BETWEEN R.start_date AND R.end_date)
GROUP BY product_id;