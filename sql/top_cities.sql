SELECT
    city,
    COUNT(*) AS total_jobs
FROM jobs
WHERE city IS NOT NULL
GROUP BY city
ORDER BY total_jobs DESC
LIMIT 10;