// const input=fs.readFileSync('/dev/stdin').toString();


const input = require('fs').readFileSync("../input.txt").toString().trim().split('\n');

const num = parseInt(input[0])

const xStr = input[1].split(' ')

const xInt = xStr.map(x => parseInt(x))

let min = xInt[0]
let max = xInt[0]

xInt.map(a => {
  // console.log('array', a);
  if(a < min) min = a 
  else if (a > max) max = a
})

console.log(min, max);