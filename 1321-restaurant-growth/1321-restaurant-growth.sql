-- This query calculates the average amount spent by a customer in a 7-day window


SELECT visited_on,  -- Select visit date
       amount,     -- Select total amount spent in the 7-day window
       ROUND(amount / 7, 2) AS average_amount  -- Calculate and round the average amount spent per 7 days
FROM (
    -- Subquery (aliased as 't'):
    SELECT DISTINCT 
        visited_on,  -- Select the distinct visit dates
        -- Calculate the sum of amount within a 7-day window for each visit
        SUM(amount) OVER (ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount,  
        MIN(visited_on) OVER () AS 1st_date  -- Find the minimum visit date across all rows (used for filtering later)
    FROM Customer -- Source table containing customer visit data (date and amount)
) t  -- Use the results from the subquery aliased as 't'
-- Main query:
WHERE visited_on >= 1st_date + INTERVAL 6 DAY;  -- Filter for visits on or after the 7th day from the first visit date

-- With Each_Day AS(SELECT 
--     visited_on,
--     SUM(amount) AS amount
-- FROM Customer
-- GROUP BY visited_on)

-- SELECT 
--     c1.visited_on,
--     SUM(c2.amount) amount,
--     ROUND(AVG(c2.amount), 2) average_amount
-- FROM Each_Day AS c1
-- JOIN Each_day AS c2
-- ON c2.visited_on <= c1.visited_on
-- AND DATEDIFF(c1.visited_on, c2.visited_on) < 7
-- GROUP BY c1.visited_on
-- HAVING COUNT(*) = 7
-- ORDER BY visited_on ASC