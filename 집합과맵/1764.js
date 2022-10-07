let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')

const firstElem = input[0].split(' ')

const N = Number(firstElem[0])
const M = Number(firstElem[1])

const arrA = []
const arrB = []
let resultArr = []
let resultNum = 0



for (let i = 1; i <= N; i++) {
  arrA.push(input[i])
}

for (let j = 1+N; j <= M+N; j++) {
  arrB.push(input[j])
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (arrA[i] === arrB[j]) {
      resultNum ++
      resultArr.push(arrA[i]) 
    }
  }
}

resultArr.unshift(resultNum)



resultArr.map(x => console.log(x))
