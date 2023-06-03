# Write your MySQL query statement below
# SELECT R.id
# FROM Weather R, Weather L
# WHERE R.EXTRACT(YEAR_DAY, recordDate) - L.EXTRACT(YEAR_DAY, recordDate) = 1;
#     # AND EXTRACT(DAY, R.recordDate) - EXTRACT(DAY, L.recordDate) = 1
#     # AND R.temperature - L.temperature > 0;

SELECT L.id
FROM Weather L, Weather R
WHERE DATEDIFF(L.recordDate, R.recordDate) = 1
    AND L.recordDate > R.recordDate
    AND L.temperature > R.temperature;