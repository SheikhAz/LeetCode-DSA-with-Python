-- Write your PostgreSQL query statement below
SELECT 
r.contest_id ,
ROUND(
    COUNT(r.user_id) * 100.00 / (SELECT COUNT(*) FROM Users)
,2) AS percentage
FROM Register AS r
JOIN Users AS u
ON r.user_id = u.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC ,r.contest_id;