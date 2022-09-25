let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');

const num = Number(input[0])

let person


for (let i = 1; i <= num; i++) {
  person = input[i].split(' ').map(x => Number(x))
}

let ranking = 1
let rankingArr = []

for (let i = 0; i < person.length; i++ ) {
  let weight = 10
  let height = 0
  if (person[0] >= weight && person[1] >= height) {
    
  }
}
