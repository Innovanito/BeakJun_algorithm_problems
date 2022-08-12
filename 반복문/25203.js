// const input=fs.readFileSync('/dev/stdin').toString();

const fs = require('fs');

let input = require('fs').readFileSync("../input.txt").toString().split('\n');

let totalAmount = parseInt(input[0])

let totalNum = parseInt(input[1])

let result = 0

for (let i = 0; i < totalNum; i++) {
  let a = input[2 + i].split(' ')
  result += parseInt(a[0]) *  parseInt(a[1])
}

if (result == totalAmount) {
  console.log('Yes');
} else {
  console.log('No');
}