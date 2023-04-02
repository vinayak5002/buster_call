const stdin = require('fs').readFileSync(0, 'utf-8');
const [a, b, c] = stdin.split(' ').map(Number);
const compare = (a < b) && (b < c) ? 'Yes' : 'No';

console.log(compare);
