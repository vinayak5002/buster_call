const stdin = require('fs').readFileSync(0, 'utf-8');
const datasets = stdin.trim('\n').split('\n');

datasets.forEach((set) => {
  const [a, b] = set.split(' ').map(Number);
  if (a === 0 && b === 0) return;
  if (a < b) console.log(a, b);
  else console.log(b, a);
});
