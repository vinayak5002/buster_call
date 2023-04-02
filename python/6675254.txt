const stdin = require('fs').readFileSync(0, 'utf-8');
const [n, a] = stdin.split('\n');
const i = a.split(' ').map(Number);
let min = Infinity;
let max = -Infinity;
let sum = 0;

i.forEach((i) => {
  if (min > i) min = i;
  if (max < i) max = i;
  sum = sum + i;
});

console.log(min, max, sum);
