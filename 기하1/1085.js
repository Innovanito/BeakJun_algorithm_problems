// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = require("fs").readFileSync("../input.txt").toString().trim().split(/\s/);

console.log(input)

const x = Number(input[0])
const y = Number(input[1])
const w = Number(input[2])
const h = Number(input[3])

const x1 = w - x
const y1 = h - y

const findMinDistance = (x,y,x1,y1) => {
    let min = x
    if (y < min) min = y
    if (x1 < min) min = x1
    if (y1 < min) min = y1
    return min
}

console.log(findMinDistance(x,y,x1,y1))