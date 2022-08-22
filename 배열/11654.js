// const input=fs.readFileSync('/dev/stdin').toString();

const input = require('fs').readFileSync("../input.txt").toString().split('\n');

const totalInput = parseInt(input[0])

let sum=0

for (let i = 0; i < totalInput; i++) {
  sum += parseInt(input[1][i])
}

console.log(sum);