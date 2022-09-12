// let input = fs.readFileSync('/dev/stdin').toString().split('\n');


let fs = require('fs');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');

let num = Number(input)

let i =2
let primeArr = []
for (i; i <= num; i++) {
  if (num % i === 0) {
    num = num / i
    primeArr.push(i)
    i = 1
  }
}

primeArr.map(x => {
  console.log(x);
})