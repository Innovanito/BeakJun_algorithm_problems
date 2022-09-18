
let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');

let num = Number(input[0])

const fibo = n => {
  if(n===0) return 0
  else if (n ===1) return 1
  else return fibo(n-1) + fibo(n-2)
}

console.log(fibo(num));