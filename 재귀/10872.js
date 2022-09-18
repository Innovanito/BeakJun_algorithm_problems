// let input = fs.readFileSync('/dev/stdin').toString().split('\n');


let fs = require('fs');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');

let num = Number(input[0])


let result = 1

const recall = (num) => {
  if (num > 0) {
    result *= num
    num -= 1
    if(num > 0) recall(num)
    return result
  }
  else if(num === 0) return result
}

console.log(recall(num));