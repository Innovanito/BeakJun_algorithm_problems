let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')

const arrA = input[1].split(' ').map(x => Number(x))
const arrB = input[3].split(' ').map(x => Number(x))

let result = []

for (let i = 0; i < arrB.length; i++) {
  for (let j = 0; j < arrA.length; j++) {
    if (arrB[i] === arrA[j]) {
      result.push(1)
      break
    } else if (arrB[i] !== arrA[j] && arrA.length - 1 === j) {
      result.push(0)
    } else continue
  }
}


console.log(result.join(" "));