// const input=fs.readFileSync('/dev/stdin').toString();

const input = require('fs').readFileSync("../input.txt").toString();

let cnt = 0
for (let char of input) {
  if(char == 'A' || char =='B' ||char == 'C' )  cnt += 3
  else if (char == 'D' || char =='E' ||char == 'F' ) cnt +=4
  else if (char == 'G' || char =='H' ||char == 'I' ) cnt +=5
  else if (char == 'J' || char =='K' ||char == 'L' ) cnt +=6
  else if (char == 'M' || char =='N' || char =='O' ) cnt +=7
  else if (char == 'P' || char =='Q' || char =='R' ||char == 'S' ) cnt +=8
  else if (char == 'T' || char =='U' || char =='V' ) cnt +=9
  else if (char == 'W' || char =='X' || char =='Y' || char =='Z' ) cnt +=10
}

console.log(cnt);