SELECT
    company,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY company
ORDER BY total_jobs DESC
LIMIT 10;