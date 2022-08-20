// const input=fs.readFileSync('/dev/stdin').toString();


const input = require('fs').readFileSync("../input.txt").toString().trim().split('\n');

const xInt = input.map(x => parseInt(x))

let max = xInt[0]

let where = 0

xInt.map((a,i) => {
  if (a > max) max = a

  where = i

})

console.log(max);
console.log(where);
