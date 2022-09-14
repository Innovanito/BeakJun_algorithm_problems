const fs = require('fs');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');

let arrNum = input.map(x => Number(x))

const totalNum = Number(input[0])

arrNum.shift()


let arrX =[]

for (let i = 0; i < totalNum-1; i++) {
  for (let j = 0; j < totalNum-1-i; j++) {
    if (arrNum[j] > arrNum[j + 1]) {
      let temp =arrNum[j]
      arrNum[j] = arrNum[j+1]
      arrNum[j+1] = temp
    }
  }
}

arrNum.map(x => {
  console.log(x);
})