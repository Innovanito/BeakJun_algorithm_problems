let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')

const inputNum = Number(input[0])

//calculate the area of circle using radius
const area = (r) => {
  return r * r * Math.PI
}

//calculate the area of eucliud using radius
const eucliud = (r) => {
  return r * r * 2
}

console.log(area(inputNum).toFixed(6));
console.log(eucliud(inputNum).toFixed(6));