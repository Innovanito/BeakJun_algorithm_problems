let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')


const a = input[0].split(' ').map(x => Number(x))

const N = a[0]

const M = a[1]

let cnt = 0


for (let i = 1; i <= N; i++) {
  for (let j = N + 1; j <= M + N; j++) {
    if(input[i] === input[j]) cnt++
  }
}

console.log(cnt);