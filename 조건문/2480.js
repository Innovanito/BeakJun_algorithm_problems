const fs = require('fs');

const input = fs.readFileSync("../input.txt").toString().trim().split('\n');

const dice = input[0].split(' ').map(Number);

const dice0 = dice[0];
const dice1 = dice[1];
const dice2 = dice[2];

let result, order

if (dice0 === dice1 && dice1 === dice2) {
  parseInt(dice0)
  result = 10000 + dice0 * 1000
  console.log(result);
}
else if (dice0 === dice1) {
  parseInt(dice0)
  result = 1000 + dice0 * 100
  console.log(result);
}
else if (dice1 === dice2) {
  parseInt(dice1)
  result = 1000 + dice1 * 100
  console.log(result);
}
else if (dice0 === dice2) {
  parseInt(dice0)
  result = 1000 + dice0 * 100
  console.log(result);
} else {
  order = dice.sort()
  result = order[2] * 100
  console.log(result);
}
