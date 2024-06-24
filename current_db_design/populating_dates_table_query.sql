INSERT INTO dates (date, day, month, year, weekday)
SELECT
    d::DATE AS date,
    EXTRACT(DAY FROM d::DATE) AS day,
    EXTRACT(MONTH FROM d::DATE) AS month,
    EXTRACT(YEAR FROM d::DATE) AS year,
    TO_CHAR(d::DATE, 'Day') AS weekday
FROM
    GENERATE_SERIES(DATE '2024-06-01', DATE '2024-06-07', INTERVAL '1 day') AS gs(d)
ON CONFLICT (date) DO NOTHING;
