// let input = fs.readFileSync('/dev/stdin').toString().split('\n');


let fs = require('fs');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n');

console.log(input);

// 먼저 범위 내 최대 자연수까지 소수를 구한다.
// 범위 내에 있는 소수를 배열으로 담는다
// 배열의 합을 구한다 ->a
// 배열의 첫번째 값을 저장한다 -> b
// a와 b를 출력한다.