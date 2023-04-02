const stdin = require('fs').readFileSync(0, 'utf-8');
const [a, b] = stdin.split(' ').map(Number);
const area = a * b;
const perimeter = 2 * (a + b);

console.log(area, perimeter);
