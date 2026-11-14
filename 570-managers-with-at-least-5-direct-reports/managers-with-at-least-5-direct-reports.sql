-- Write your PostgreSQL query statement below
SELECT e.name 
FROM Employee AS e
JOIN Employee AS m
ON e.id = m.managerId
GROUP BY e.id,e.name 
HAVING COUNT(m.id) >= 5;