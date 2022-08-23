const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');
let S = input[0]; //단어: baekjoon
let S_arr = S.split('');
let array = ['a','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z'];
let answer = '';
let r_arr = [];
let count = 0;

for(let i =0; i < array.length; i++) {
    let count = 0;
    for(let j=0; j < S_arr.length; j++) {
        if(array[i] === S_arr[j]) {
            // if(array[i])
            r_arr.push(j)
            break;
        } else {
            count++;
        }
    }
    if(count === S_arr.length) {
        r_arr.push(-1);
    }
}

for(let i=0; i < r_arr.length; i++) {
    answer += r_arr[i] + ' ';
}
console.log(answer);