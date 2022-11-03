let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')

for (let i = 0; i < input.length; i++) {
  let result
  let nums = input[i].split(' ').map(x => Number(x))
  let a = nums[0]
  let b = nums[1]
  if (a === 0 && b === 0) {
    break
  }
  if (b % a === 0) {
    result = 'factor'
  } else if (a % b === 0) {
    result = 'multiple'
  } else {
    result = 'neither'
  }
  console.log(result)
}

