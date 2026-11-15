SELECT
s.user_id,
ROUND(
    COALESCE(
        COUNT(c.action) FILTER (WHERE c.action = 'confirmed')::numeric 
        /NULLIF(COUNT(c.action),0)
    ,0)
,2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c
ON c.user_id = s.user_id
GROUP BY s.user_id;