# Write your MySQL query statement below
# SELECT DISTINCT player_id, min(event_date) as first_login
# FROM Activity
# GROUP BY player_id, event_date;


SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;