// const input=fs.readFileSync('/dev/stdin').toString();

const input = require('fs').readFileSync("../input.txt").toString().trim().split('\n');

const totalInput = parseInt(input[0])

input.shift()

let sum = 0

for (let i = 0; i < input.length; i++) {
  let str = input[i]
  let cnt = 0
  for (let j = 0; j < str.length; j++) {
    if (str[j] === 'O') {
      cnt++
      sum += cnt
    }
    else cnt = 0
  }

  console.log(sum);
  sum = 0
}
