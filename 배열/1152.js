// const input=fs.readFileSync('/dev/stdin').toString();

const input = require('fs').readFileSync("../input.txt").toString().trim().split(' ');

if (input == '') console.log(0);

else console.log(input.length);