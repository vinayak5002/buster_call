const stdin = require('fs').readFileSync(0, 'utf-8');
let [a, b, c] = stdin.split(' ').map(Number);

if (a > b) {
  const temp = a;
  a = b;
  b = temp;
}

if (b > c) {
  const temp = b;
  b = c;
  c = temp;
}

if (a > b) {
  const temp = a;
  a = b;
  b = temp;
}

console.log(a, b, c);
