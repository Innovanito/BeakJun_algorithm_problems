// let input = fs.readFileSync('/dev/stdin').toString().split('\n');


let fs = require('fs');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');
let cases = Number(input[0])
let splited = input[1].split(' ').map((item) => Number(item))
let answer = 0

console.log('input', input);
console.log('splited', splited);

for (let i = 0; i < splited.length; i++) {
  if (splited[i] === 1) {
    continue
  }
  else {
    let count = 0
    for (let j = 2; j < splited[i]; j++) {
      if (splited[i] % j === 0) {
        count++
      }
    }
    if (count === 0) {
      answer++
    }
  }
}

console.log(answer);