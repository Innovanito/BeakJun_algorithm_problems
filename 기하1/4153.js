let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')

const inputLength = input.length
let arr =[]
let answer = []

for (let i = 0; i < inputLength; i++) {
  if (input[i] === '0 0 0') {
    break
  } else {
    arr[i] = input[i].split(' ').map(x => Number(x))
  }
}

for (let i = 0; i < arr.length; i++) {
  if (arr[i][0] ** 2 + arr[i][1] ** 2 === arr[i][2] ** 2) {
    answer.push('right')
  } else if (arr[i][0] ** 2 + arr[i][2] ** 2 === arr[i][1] ** 2) {
    answer.push('right')
  } else if (arr[i][1] ** 2 + arr[i][2] ** 2 === arr[i][0] ** 2) {
    answer.push('right')
  } else {
    answer.push('wrong')
  }
}



answer.map(x=> console.log(x))