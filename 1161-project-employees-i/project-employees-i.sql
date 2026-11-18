-- Write your PostgreSQL query statement below
SELECT 
p.project_id,
COALESCE(
    ROUND(
        SUM(e.experience_years)::numeric / COUNT(e.employee_id)
    ,2) ,0
) AS average_years
FROM Project AS p
LEFT JOIN Employee AS e
ON e.employee_id = p.employee_id
GROUP BY p.project_id
ORDER BY p.project_id;