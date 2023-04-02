const stdin = require('fs').readFileSync(0, 'utf-8');
const [W, H, x, y, r] = stdin.split(' ').map(Number);

if ((x - r) >= 0 && (y - r) >= 0 && (x + r) <= W && (y + r) <= H) {
  console.log('Yes');
} else {
  console.log('No');
}
