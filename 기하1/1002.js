let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')

const inputLength = Number(input[0])


for (let i = 0; i < inputLength; i++) {
  let result 

  let cordinate = input[i + 1].split(' ').map(x => Number(x))
  let x1 = cordinate[0]
  let y1 = cordinate[1]
  let x2 = cordinate[2]
  let y2 = cordinate[3]
  let r1 = cordinate[4]
  let r2 = cordinate[5]

  // distance 1 is the distance between the center of the circle and the center of the circle
  let distance1 = Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
  
  //distance2 is the absolute value of r1 + r2
  let distance2 = Math.abs(r1 + r2)

  console.log(distance1, distance2);

  //if the distance1 is 0 and r1 and r2 are the same, result is -1
  if (distance1 === 0 && r1 === r2) {
    result = -1
  }
  //if the distance1 is greater than distance2, result is 0
  else if (distance1 > distance2) {
    result = 0
  }
  //if the distance1 is equal to distance2, result is 1
  else if (distance1 === distance2) {
    result = 1
  }
  //if the distance1 is less than distance2, result is 2
  else if (distance1 < distance2) {
    result = 2
  }

  console.log(result)
}