// const input=fs.readFileSync('/dev/stdin').toString();


let input = require('fs').readFileSync('../input.txt').toString().split('\n');

let a = input[0].split(' ')

let count = parseInt(a[0])

let ref = parseInt(a[1])

let varNum = input[1].split(' ')

let result = ''

for (let i = 0; i < count; i++) {
  if (parseInt(varNum[i]) <ref) {
    result += varNum[i] + ' '
  }
}

console.log(result);