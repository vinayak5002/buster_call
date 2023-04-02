const stdin = require('fs').readFileSync(0, 'utf-8');
const numbers = stdin.split('\n').map(Number).filter((num) => num !== 0);

numbers.forEach((num, i) => {
  console.log('Case', (i + 1) + ':', num);
});
