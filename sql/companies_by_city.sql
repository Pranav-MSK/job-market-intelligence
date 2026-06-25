SELECT
    city,
    company,
    COUNT(*) AS total_jobs
FROM jobs
WHERE city IS NOT NULL
GROUP BY city, company
ORDER BY total_jobs DESC;