// const input=fs.readFileSync('/dev/stdin').toString();


let input = require('fs').readFileSync("../input.txt").toString().split('\n');

let totalAmount = parseInt(input[0])

let result = ''


for (let i = 0; i < totalAmount; i++) {
  sum = 0
  let a = input[1 + i].split(' ')
  sum += parseInt(a[0]) +  parseInt(a[1]) 
  result += `Case #${i+1}: ${sum} \n`
}

console.log(result);
