# Write your MySQL query statement below
# 순위 매기는 규칙. 1) 내림차순 2) 동점이 있으면 같은 순위
# 3) 동점자가 있어도 순위는 순차적으로 내려감

# discuss 보고 얻은 힌트. 대소비교 조건으로 랭크에 넣고, 카운트하기

# SELECT score, (SELECT COUNT(*) FROM (SELECT DISTINCT score FROM Scores) AS TMP WHERE score >= TMP.score) AS rank
# FROM Scores
# ORDER BY score DESC;

SELECT L.score,
        (SELECT COUNT(DISTINCT R.score) FROM Scores R WHERE L.score <= R.score) AS 'rank'
FROM Scores L
ORDER BY L.score DESC;