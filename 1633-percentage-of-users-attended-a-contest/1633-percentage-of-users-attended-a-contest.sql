# Write your MySQL query statement below
SELECT 
contest_id, 
ROUND(COUNT(DISTINCT user_id) * 100 /(SELECT COUNT(user_id) from Users) ,2) as percentage
from  Register
group by contest_id
order by percentage desc,contest_id asc