// const input=fs.readFileSync('/dev/stdin').toString();

const input = require('fs').readFileSync("../input.txt").toString().split('\n');

const totalInput = parseInt(input[0])

input.shift()

let sum = 0

let avg = 0

let overScore = 0

for (let i = 0; i < input.length; i++) {
  let arr = input[i].split(' ')
  arr.shift()
  for (let j = 0; j < arr.length; j++) {
    sum += parseInt(arr[j])
  }
  avg = sum / arr.length

  for (let j = 0; j < arr.length; j++) {
    if(parseInt(arr[j]) > avg) overScore++
  }

  let res = (overScore/arr.length * 100).toFixed(3)
  console.log(res+'%');
  sum = 0
  avg = 0
  overScore=0
}

