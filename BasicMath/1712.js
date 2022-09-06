let fs = require('fs');
let input = fs.readFileSync('../input.txt').toString().trim().split(' ');

// (a + b * x) < c * x 인 최소 자연수 x? (없으면 -1)

let a = parseInt(input[0])
let b = parseInt(input[1])
let c = parseInt(input[2])

let rev = a/(c-b)

let solution

if (b == c) solution = -1
else {
  if(rev <= 0 ) solution = -1
  else {
    if(Number.isInteger(rev)) solution = rev +1
    else solution = Math.ceil(rev)
  }
}


console.log(solution);
