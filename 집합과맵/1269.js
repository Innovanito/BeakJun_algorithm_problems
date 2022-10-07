let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')

const arrA = input[1].split(' ')
const arrB = input[2].split(' ')

let sameElem = 0

arrA.map(x => {
  arrB.map(y => {
    if(x === y) sameElem ++ 
  })
})



console.log(arrA.length + arrB.length - sameElem * 2);