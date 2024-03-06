# Write your MySQL query statement below
# sum of all total investment values in 2016 tiv_2016
# have the same tiv_2015 value as one or more other policyholders, and
# are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique)
# Round tiv_2016 to two decimal places.
# Approach 1: Subqueries
-- SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
-- FROM insurance
-- WHERE tiv_2015 IN (
--     SELECT tiv_2015
--     FROM Insurance
--     GROUP BY tiv_2015
--     HAVING COUNT(DISTINCT pid) > 1
-- )
-- AND 
--     CONCAT(lat, lon) IN (
--         SELECT CONCAT(lat, lon) as lat_lon
--         FROM Insurance
--         GROUP by CONCAT(lat, lon)
--         HAVING COUNT(Distinct pid) = 1
-- )


# Approach 2: Window Functions
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
   SELECT *,
       COUNT(*)OVER(PARTITION BY tiv_2015) AS tiv_2015_cnt,
       COUNT(*)OVER(PARTITION BY lat, lon) AS loc_cnt
   FROM Insurance
   )t0
WHERE tiv_2015_cnt > 1
AND loc_cnt = 1