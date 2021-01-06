/*
programmers : 상위 N개 레코드
solved by JY
DATE : 2021.01.06
*/
SELECT  NAME
FROM    ANIMAL_INS
WHERE   DATETIME = (
                SELECT MIN(DATETIME) 
                FROM ANIMAL_INS
        );
