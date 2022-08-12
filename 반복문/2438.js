// const input=fs.readFileSync('/dev/stdin').toString();

let input = require('fs').readFileSync("../input.txt").toString().split('\n');

let num = parseInt(input[0])


for (let i = 1; i <= num; i++) {
  star = ''
  for (let j = 0; j < i; j++) {
    star += '*' 
  }
  console.log(star);
}

