// const input=fs.readFileSync('/dev/stdin').toString();


const input = require('fs').readFileSync("../input.txt").toString().trim().split('\n');

const totalInput = parseInt(input[0])

const element = input[1].split(' ')

const elementInt = element.map(x => parseInt(x))

let maxNum = elementInt[0]

let maxInt = elementInt.map(x => {
  if (x > maxNum)  maxNum = x
})

let newElement = elementInt.map(x => 
  x / maxNum * 100
)

let sum = 0

newElement.map(x => sum += x) 

let result = sum / totalInput

console.log(result);