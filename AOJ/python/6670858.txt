const stdin = require('fs').readFileSync(0, 'utf-8');
const r = parseFloat(stdin);
const area = (Math.PI * r * r).toFixed(8);
const circumference = (2 * Math.PI * r).toFixed(8);

console.log(area, circumference);
