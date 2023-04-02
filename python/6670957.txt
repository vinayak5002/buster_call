const stdin = require('fs').readFileSync(0, 'utf-8');
const operations = stdin.split('\n');

operations.forEach((operation) => {
  const [a, op, b] = operation.split(' ');

  if (!op || op === '?') return;

  const sum = Math.floor(eval(operation));
  console.log(sum);
});
