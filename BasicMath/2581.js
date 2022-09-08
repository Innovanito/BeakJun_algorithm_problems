// let input = fs.readFileSync('/dev/stdin').toString().split('\n');


let fs = require('fs');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');

const minNum = Number(input[0])
const maxNum = Number(input[1])

let primeArr =[]
let arrWanted = []
let arrSum = 0

const findPrime = (b) => {
  for (let i = 2; i <= b; i++) {
    let isPrime = 1
    for (let j = 2; j < i; j++) {
      if (i % j === 0) {
        isPrime = 0
        break
      }
      else continue
    }
    if(isPrime) primeArr.push(i)
  }
}

findPrime(maxNum)

primeArr.map(arr => {
  if(arr>= minNum) arrWanted.push(arr)
  }
)

arrWanted.map(arr => {
  arrSum += Number(arr)
})

if (arrWanted.length === 0) console.log('-1');
else {
  console.log(arrSum);
  console.log(arrWanted[0]);
}


// 먼저 범위 내 최대 자연수까지 소수를 구한다.
// 범위 내에 있는 소수를 배열으로 담는다
// 배열의 합을 구한다 ->a
// 배열의 첫번째 값을 저장한다 -> b
// a와 b를 출력한다.