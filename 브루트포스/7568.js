let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');

const N = Number(input.shift());
let person = [];
let finalArr = [];

for (let i = 0; i < N; i++) {
  let temp = input[i].split(' ');
  person.push(temp);
}

solution();

function solution() {
  for (let i = 0; i < N; i++) {
    let count = 0;

    for (let j = 0; j < N; j++) {
      if (person[i][0] < person[j][0]) {
        if (person[i][1] < person[j][1]) {
          count++;
        }
      }
    }
    finalArr.push(String(count + 1));
  }
  console.log(finalArr.join(' '));
}

