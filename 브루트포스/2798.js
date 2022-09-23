let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');

const firstArr = input[0].split(' ')
const N = Number(firstArr[0])
const M = Number(firstArr[1])
const numArr = input[1].split(' ').map(x => parseInt(x))

let sumVal
let finalVal = 0 

for (let i = 0; i < N; i++){
  let firstNum = numArr[i]
  for (let j = 1 + i; j < N; j++) {
    let secondNum = numArr[j]
    for (let z = 1 + j; z < N; z++) {
      let thirdNum = numArr[z]
      sumVal = firstNum + secondNum + thirdNum
      if(sumVal <= M && sumVal > finalVal) finalVal = sumVal
    }
  }
}

console.log(finalVal);

// 0. 카드 개수 N과 최대값 M을 생성한다.
// 1. 2번째 줄의 값들을 배열으로 생성한다
// 2. 배열에서 3 값을 선택한다. ->반복문 3번을 사용하자
// 3. 선택한 3 값을 더한 변수 sumVal 생성한다
// 3.5 finalVal = 0 으로 생성
// 4. if(sumVal <= M && sumVal > finalVal) finalVal = sumVal

