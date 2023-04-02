const stdin = require('fs').readFileSync(0, 'utf-8');
const timestamp = parseInt(stdin);
const seconds = timestamp % 60;
const minutes = Math.floor(timestamp / 60 % 60);
const hours = Math.floor(timestamp / 3600);

console.log(hours + ':' + minutes + ':' + seconds);
