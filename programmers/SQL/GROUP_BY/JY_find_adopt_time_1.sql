-- 코드를 입력하세요
-- 데이턱가 있는 시간만 출력
SELECT  hour, count(*) count
FROM 
    (SELECT TO_CHAR(datetime, 'hh24') hour
    FROM animal_outs) time
WHERE   hour >= 9 and hour < 20
GROUP BY hour
ORDER BY hour;