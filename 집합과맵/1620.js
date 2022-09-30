let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')

const numArr = input[0].split(' ')

const numA = Number(numArr[0])
const numB = Number(numArr[1])

let dic = []
let problem = []
let result = []

// 도감 포캣몬을 dic에 push
for (let i = 1; i <= numA; i++) {
  dic.push(input[i])
}
// 문제를 problem에 push
for (let j = numA + 1; j <= numA + numB ; j++){
  if(Number(input[j]) > 0) problem.push(Number(input[j]))
  else problem.push(input[j])
}

problem.map(x => {
  if (typeof x === 'number') {
    result.push(dic[x-1])
  } else {
    for (let z = 0; z < dic.length; z++) {
      if(dic[z] === x) result.push(z+1)
    }
  }
})

result.map(x => console.log(x))