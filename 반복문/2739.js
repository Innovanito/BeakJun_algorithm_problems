const fs = require('fs');

const input = fs.readFileSync("../input.txt").toString().trim().split('\n');

num = parseInt(input)

let i

for (i = 1; i < 10; i++) {
  console.log(num ,'*', i, '=' ,num*i,'\n');
}