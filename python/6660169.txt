const stdin = require('fs').readFileSync(0, 'utf-8');
const [a, b] = stdin.split(' ').map(Number);
const sign = a < b ? '<' : a > b ? '>' : '==';

console.log('a', sign, 'b');
