CREATE FUNCTION InsertDatesFromSales()
RETURNS VOID AS
$$
BEGIN
    INSERT INTO Dates (date, day, month, year, weekday)
    SELECT DISTINCT 
        event_date::DATE,
        EXTRACT(DAY FROM event_date) AS day,
        EXTRACT(MONTH FROM event_date) AS month,
        EXTRACT(YEAR FROM event_date) AS year,
        TO_CHAR(event_date, 'Day') AS weekday
    FROM sales
    ON CONFLICT (date) DO NOTHING;
END;
$$
LANGUAGE plpgsql;