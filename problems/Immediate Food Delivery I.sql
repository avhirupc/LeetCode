# Write your MySQL query statement below
select ROUND((COUNT(delivery_id)/(select COUNT(delivery_id) from delivery))*100,2) as immediate_percentage
from delivery
where order_date=customer_pref_delivery_date
