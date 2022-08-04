const fs = require('fs');

const [h, m, x] = fs.readFileSync('../input.txt').toString().trim().split('\n').map(Number);

let new_h,new_m, h_x 

new_m = m + x

for (; new_m > 60; new_m - 60) {
  h_x ++
}

new_h = h + h_x

if (new_h >= 24) {
  new_h -=24
}

if (new_h >= 24) {
  new_h -=24
}

console.log(new_h, new_m );

