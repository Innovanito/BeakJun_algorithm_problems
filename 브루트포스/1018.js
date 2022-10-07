let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let input = fs.readFileSync("../input.txt").toString().trim().split("\n");

const NM = input.shift().split(" ");
const N = Number(NM.shift());
const M = Number(NM.shift());
const candidates = [];


// for (let i = 0; i + 7 < N; i++) {
//   console.log(i);
// }

  for (let i = y; i < y + 8; i++) {
    for (let j = x; j < x + 8; j++) {
      if (input[i][j] !== whiteFirstBoard[i - y][j - x]) {
        count++;
      }
    }
  }