/*
baekjoon 10998 : A×B
solved by JY
DATE : 2021.01.20
*/

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', function(line) {
    input = line.split(" ");
    console.log(input[0] * input[1]);
    
    rl.close();
}).on("close", function() {
    process.exit();
});