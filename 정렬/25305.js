const fs = require('fs');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');

const inputLine1 = input[0].split(' ');
const inputLine2 = input[1].split(' ');

const people = Number(inputLine1[0]);

const cutline = Number(inputLine1[1]);

let scoreArr = inputLine2.map(x => Number(x));

const sort = (arr) => {
  for (let i = 0; i < people - 1; i++) {
    for (let j = 0; j < people - 1 - i; j++){
      if (arr[j] < arr[j + 1]) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}

console.log(sort(scoreArr)[cutline-1]);
