const stdin = require('fs').readFileSync(0, 'utf-8');
const numbers = stdin.split(' ').map(Number);
const sorted = numbers.sort((a, b) => a - b);

console.log(sorted.join(' '));
