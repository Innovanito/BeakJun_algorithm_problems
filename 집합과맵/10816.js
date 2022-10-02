let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')

const N = Number(input[0]) 
const M = Number(input[2])

let arr1 = input[1].split(' ').map(x => Number(x))
let arr2 = input[3].split(' ').map(x => Number(x))

let result = []

for (let i = 0; i < arr2.length; i++) {
  let cnt = 0
  for (let j = 0; j < arr1.length; j++) {
    if (arr2[i] === arr1[j]) cnt++
    if(j === arr1.length - 1) result.push(cnt)
  }
}

console.log(result.join(' '));