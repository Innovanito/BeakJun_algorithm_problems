// const input=fs.readFileSync('/dev/stdin').toString();


let input = require('fs').readFileSync('../input.txt').toString().split('\n');


input.map(a => {
  let b = a.split(' ')
  console.log(parseInt(b[0]) + parseInt(b[1]));
})
