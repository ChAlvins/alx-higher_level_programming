-- import temperatures into hbtn_0c_0
-- Displays the average temperature (in Fahrenheit)
-- by city ordered by descending temperature.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
