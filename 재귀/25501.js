let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');

const num = Number(input[0])

let cnt = 0

const recursion = (s, l, r) => {
  cnt ++ 
  if (l >= r) return 1
  else if (s[l] != s[r]) return 0
  else {
    return recursion(s, l + 1, r - 1)
  }
}

const isPalindrome = (s) => {
  return recursion(s,0, s.length-1)
}

for (let i = 1; i <= num; i++) {
  let str = input[i]
  console.log(`${isPalindrome(str)} ${cnt}`);
  cnt = 0
}