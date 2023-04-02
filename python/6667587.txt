const stdin = require('fs').readFileSync(0, 'utf-8');
const [a, b, c] = stdin.split(' ').map(Number);
let divisors = 0;

for (let i = a; i <= b; i++) {
  if (c % i === 0) divisors++;
}

console.log(divisors);
