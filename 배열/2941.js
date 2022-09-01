// const input=fs.readFileSync('/dev/stdin').toString();

const input = require('fs').readFileSync("../input.txt").toString();

let regExp = /c\=|c\-|dz\=|d\-|lj|nj|s\=|z\=/g;
let result = input.replace(regExp, '-')
console.log(result);