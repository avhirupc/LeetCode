# Write your MySQL query statement below
select prices.product_id, ROUND(SUM(unitssold.units*prices.price)/SUM(unitssold.units),2) as average_price
from prices
join unitssold
on (prices.product_id=unitssold.product_id) AND (unitssold.purchase_date between prices.start_date AND prices.end_date)
group by product_id