SELECT
    COUNT(*) AS remote_jobs
FROM jobs
WHERE LOWER(description) LIKE '%remote%';