SELECT
    country,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY country
ORDER BY total_jobs DESC;