const fs = require('fs');
let input = fs.readFileSync('../input.txt').toString().trim().split(' ');

let startNum = Number(input[0])
let endNum = Number(input[1])

let primeArr = []

for (startNum; startNum <= endNum; startNum++) {
  for (let i = 2; i <= startNum; i++) {
    if (i === startNum) {
      primeArr.push(i)
    }

    else if (startNum % i === 0) {
      break
    }
  }
}

primeArr.map(x => {
  console.log(x);
})