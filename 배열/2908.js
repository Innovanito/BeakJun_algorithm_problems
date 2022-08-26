// const input=fs.readFileSync('/dev/stdin').toString();

const input = require('fs').readFileSync("../input.txt").toString().split(' ');

let a = input[0]
let b = input[1]

let newA = '' 
let newB = '' 


for (let i = a.length -1 ; i >= 0 ; i--) {
  newA += a[i]
  newB += b[i]
}

console.log(parseInt(newA)> parseInt(newB) ? parseInt(newA) : parseInt(newB));