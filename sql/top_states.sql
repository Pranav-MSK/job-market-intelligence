SELECT
    state,
    COUNT(*) AS total_jobs
FROM jobs
WHERE state IS NOT NULL
GROUP BY state
ORDER BY total_jobs DESC;