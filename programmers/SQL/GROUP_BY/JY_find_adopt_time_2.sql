-- 코드를 입력하세요
WITH TIME AS (
    SELECT  LEVEL-1 HOUR
    FROM    DUAL
    CONNECT BY LEVEL <= 24
)
SELECT  T1.HOUR HOUR, count(T2.ANIMAL_ID) count
FROM    TIME T1 LEFT JOIN ANIMAL_OUTS T2
    ON  T1.HOUR = TO_CHAR(T2.DATETIME, 'HH24')
GROUP BY T1.HOUR
ORDER BY T1.HOUR;