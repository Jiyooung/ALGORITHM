/*
programmers L2 : 구명보트
solved by JY
DATE : 2020.01.20
Greedy 알고리즘
*/
function solution(people, limit) {
    var answer = 0;
    var end = people.length - 1;

    people.sort(function(a, b) { return b - a; });   // 내림차순으로 정렬
    
    for (var i=0; i <= end; i++) {
        if (people[i] + people[end] <= limit && i != end)
            end -= 1;
        answer += 1;
    }

    return answer;
}

// run test
var people = [70, 50, 80, 50]
var limit = 100
console.log(solution(people, limit))