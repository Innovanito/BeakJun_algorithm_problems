// const input=fs.readFileSync('/dev/stdin').toString();

const input = require('fs').readFileSync("../input.txt").toString().split('\n');

const allNum = parseInt(input[0])

for (let i = 1; i <= allNum; i++) {
  let x = input[i].split(' ')
  let repeat = parseInt(x[0])
  let letter = x[1]
  let res =''
  for (let j = 0; j < letter.length; j++) {
    for (let k = 0; k < repeat; k++) {
      res += letter[j]
    }
  }
  console.log(res);
}
