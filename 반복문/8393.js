// const input=fs.readFileSync('/dev/stdin').toString();


const fs = require('fs');

let input = require('fs').readFileSync("../input.txt").toString().split('\n');

let num = parseInt(input)

let result =0

for (let i = 1; i <= num; i++) {
  result += i
}

console.log(result);