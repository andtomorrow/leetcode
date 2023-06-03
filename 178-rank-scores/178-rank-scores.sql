# Write your MySQL query statement below
# 순위 매기는 규칙. 1) 내림차순 2) 동점이 있으면 같은 순위
# 3) 순위는 동점자 수의 영향을 받지 않고 순차적으로 내려감

SELECT L.score,
    (SELECT COUNT(DISTINCT R.score) FROM Scores R Where R.score >= L.score) AS 'rank'
FROM Scores L
ORDER BY L.score DESC;