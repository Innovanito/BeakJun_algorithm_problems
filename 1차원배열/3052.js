// const input=fs.readFileSync('/dev/stdin').toString();


const input = require('fs').readFileSync("../input.txt").toString().trim().split('\n');

const inputInt = input.map(x => parseInt(x))

let count 

let remainder =  inputInt.map(x => 
  x % 42
)

let result1 = [...new Set(remainder)];


console.log(result1.length);