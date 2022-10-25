let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')

const areaOutput= Number(input[0])

const side1 = input[1].split(' ').map(x => Number(x))
const side2 = input[2].split(' ').map(x => Number(x))
const side3 = input[3].split(' ').map(x => Number(x))
const side4 = input[4].split(' ').map(x => Number(x))
const side5 = input[5].split(' ').map(x => Number(x))
const side6 = input[6].split(' ').map(x => Number(x))


sideA = 0
sideB = 0
sideC = 0
sideD = 0

let index

if(side1[0] === 1) sideA++
else if(side1[0] ===2 ) sideB++
else if(side1[0] ===3 ) sideC++
else if (side1[0] === 4) sideD++

if(side2[0] === 1) sideA++
else if(side2[0] ===2 ) sideB++
else if(side2[0] ===3 ) sideC++
else if(side2[0] ===4 ) sideD++

if(side3[0] === 1) sideA++
else if(side3[0] ===2 ) sideB++
else if(side3[0] ===3 ) sideC++
else if(side3[0] ===4 ) sideD++

if(side4[0] === 1) sideA++
else if(side4[0] ===2 ) sideB++
else if(side4[0] ===3 ) sideC++
else if (side4[0] === 4) sideD++

if(side5[0] === 1) sideA++
else if(side5[0] ===2 ) sideB++
else if(side5[0] ===3 ) sideC++
else if (side5[0] === 4) sideD++

if(side6[0] === 1) sideA++
else if(side6[0] ===2 ) sideB++
else if(side6[0] ===3 ) sideC++
else if (side6[0] === 4) sideD++

// if the side1 to the side6 find first two side, index that side
while (index === 0) {
  if (side1[0] === 1 && sideA === 2) index = 1
  else if (side1[0] === 2 && sideB === 2) index = 1
  else if (side1[0] === 3 && sideC === 2) index = 1
  else if (side1[0] === 4 && sideD === 2) index = 1
}



console.log(sideA, sideB, sideC, sideD)



//find the area of hexagon
