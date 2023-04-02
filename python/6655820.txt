const stdin = require('fs').readFileSync(0, 'utf-8');
const number = parseInt(stdin);
const cubic = number * number * number;

console.log(cubic);
