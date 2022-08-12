// const input=fs.readFileSync('/dev/stdin').toString();

const fs = require('fs');


let input = require('fs').readFileSync("../input.txt").toString().split('\n');

for (let i = 1; i <= input[0]; i++) {
    let numbers = input[i].split(' ');
    
    console.log(Number(numbers[0]) + Number(numbers[1]));
}