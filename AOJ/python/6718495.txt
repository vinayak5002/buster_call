const stdin = require('fs').readFileSync(0, 'utf-8');
const [n, a] = stdin.trim('\n').split('\n');
const ai = a.split(' ').reverse().join(' ');

console.log(ai);
