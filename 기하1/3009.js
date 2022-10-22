let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = fs.readFileSync('../input.txt').toString().trim().split('\n')

const cord1 = input[0].split(' ').map(x => Number(x));
const cord2 = input[1].split(' ').map(x => Number(x));
const cord3 = input[2].split(' ').map(x => Number(x));

const findX = (cord1, cord2, cord3) => {
    if (cord1[0] === cord2[0]) return cord3[0]
    else if (cord1[0] === cord3[0]) return cord2[0]
    else return cord1[0]
}

const findY = (cord1, cord2, cord3) => {
    if (cord1[1] === cord2[1]) return cord3[1]
    else if (cord1[1] === cord3[1]) return cord2[1]
    else return cord1[1]
}

console.log(findX(cord1, cord2, cord3), findY(cord1, cord2, cord3))


