const fs = require('fs');

const [h, m] = fs.readFileSync('../input.txt').toString().trim().split('\n').map(Number);

if (h !== 0) {
  if ( m >= 0 && m < 45) console.log(h-1, m+60-45);
  else console.log(h, m-45);
} else {
  if ( m >= 0 && m < 45) console.log(23, m+60-45);
  else console.log(0, m-45);
}

