USE uber_project;
SELECT COUNT(*) AS Total_Trips
FROM trips;
SELECT SUM(Fare) AS Total_Revenue
FROM trips;
SELECT Pickup_Area, COUNT(*) AS Total_Trips
FROM trips
GROUP BY Pickup_Area
ORDER BY Total_Trips DESC;
SELECT Hour_of_Day, COUNT(*) AS Trips
FROM trips
GROUP BY Hour_of_Day
ORDER BY Trips DESC
LIMIT 1;
SELECT Pickup_Area, SUM(Fare) AS Revenue
FROM trips
GROUP BY Pickup_Area
ORDER BY Revenue DESC
LIMIT 1;
SELECT AVG(Fare) AS Average_Fare
FROM trips;
SET SQL_SAFE_UPDATES = 0;
DELETE FROM trips
WHERE Trip_ID IS NULL OR Trip_ID = '';
-- table design
DESCRIBE trips;
SELECT * FROM trips
WHERE Hour_of_Day = 19;
CREATE VIEW trip_summary AS
SELECT 
    Pickup_Area,
    COUNT(*) AS Total_Trips,
    SUM(Fare) AS Total_RevenueSELECT  
FROM trips
GROUP BY Pickup_Area;
select * FROM trip_summary;
