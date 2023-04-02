const stdin = require('fs').readFileSync(0, 'utf-8');
const [a, b] = stdin.split(' ').map(Number);
const d = Math.floor(a / b);
const r = a % b;
const f = (a / b).toFixed(8);

console.log(`${d} ${r} ${f}`);
