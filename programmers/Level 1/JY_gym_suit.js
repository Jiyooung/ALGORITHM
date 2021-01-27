/*
programmers L1 : 체육복
solved by JY
DATE : 2021.01.21
Greedy 알고리즘
*/
function solution(n, lost, reserve) {
    var answer = n;

    let re = reserve.filter(x => !lost.includes(x));
    let lo = lost.filter(x => !reserve.includes(x));

    for (var i=0; i<re.length; i++) {
        if (lo.includes(re[i] - 1)) {
            lo.splice(lo.indexOf(re[i] - 1), 1);
        } 
        else if (lo.includes(re[i] + 1)) {
            lo.splice(lo.indexOf(re[i] + 1), 1);
        }
    }

    return answer - lo.length;
}

// run test
let n = 3;
let lost = [1, 2, 3];
let reserve = [1, 2];
console.log(solution(n, lost, reserve));
