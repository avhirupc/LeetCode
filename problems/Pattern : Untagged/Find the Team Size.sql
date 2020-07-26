# Write your MySQL query statement below



select employee_id,team_size
from employee
inner join (select team_id,count(employee_id) as team_size
from employee
group by team_id) team_size_dist
on employee.team_id = team_size_dist.team_id;