/*
programmers : 입양 시각 구하기(1)
solved by JY
DATE : 2021.01.18
데이터가 있는 시간만 출력
*/
SELECT  hour, count(*) count
FROM 
    (SELECT TO_CHAR(datetime, 'hh24') hour
    FROM animal_outs) time
WHERE   hour >= 9 and hour < 20
GROUP BY hour
ORDER BY hour;