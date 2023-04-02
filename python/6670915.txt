const stdin = require('fs').readFileSync(0, 'utf-8');
const operations = stdin.split('\n');

operations.forEach((operation) => {
  let [a, op, b] = operation.split(' ');
  let sum = 0;

  [a, b] = [a, b].map(Number);

  switch (op) {
    case '+':
      sum = a + b;
      break;
    case '-':
      sum = a - b;
      break;
    case '*':
      sum = a * b;
      break;
    case '/':
      sum = Math.floor(a / b);
      break;
    default:
      return;
  }

  console.log(sum);
});
