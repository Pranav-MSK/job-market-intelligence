SELECT
    DATE(created_at) AS posting_date,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY posting_date
ORDER BY posting_date;