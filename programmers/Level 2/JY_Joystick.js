/*
programmers L2 : 조이스틱
solved by JY
DATE : 2020.01.21
Greedy 알고리즘
*/

function updown(name, idx) {
    if (name.charCodeAt(idx) - 'A'.charCodeAt() < 13)
        return name.charCodeAt(idx) - 'A'.charCodeAt();
    else
        return 'Z'.charCodeAt() - name.charCodeAt(idx) + 1;
}

// input 문자열의 index에 있는 문자를 character로 바꾸기
var replaceAt = function(input, index, character){
    return input.substr(0, index) + character + input.substr(index+character.length);
}

function solution(name) {
    var answer = 0
    let index = [];
    for (var i =0; i< name.length; i++) {
        if (name[i] != 'A')
            index.push(i);
    }
    let s =  ""
    for (var a in name)
        s += 'A'
    let cur = 0

    while(true) {
        if (name == s) break;

        // 오른쪽으로 이동
        var right = index[0] < cur ? Math.abs(index[0] + name.length - cur) : Math.abs(index[0] - cur);
        var left = index[index.length-1] < cur ? cur - index[index.length-1] : Math.abs(cur + name.length - index[index.length-1]);
        if (right <= left) {
            answer += right + updown(name, index[0])
            cur = index[0]
            index.shift()
        } else {
            answer += left + updown(name, index[index.length-1])
            cur = index[index.length-1]
            index.pop()
        }
        name = replaceAt(name, cur, "A")
    }
    return answer;
}
// run test
console.log(solution("BBBAAAB")) //9
console.log(solution("ABABAAAAABA")) //11
console.log(solution("CANAAAAANAN")) //49
console.log(solution("ABAAAAABAB")) //8
console.log(solution("ABABAAAAAB")) //10
console.log(solution("BABAAAAB")) //7
console.log(solution("AAA")) //0
console.log(solution("ABAAAAAAABA")) //6
console.log(solution("AAB")) //2
console.log(solution("AABAAAAAAABBB")) //12
console.log(solution("ZZZ")) //5
console.log(solution("BBBBAAAAAB")) //12
console.log(solution("BBBBAAAABA")) //13