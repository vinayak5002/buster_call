const stdin = require('fs').readFileSync(0, 'utf-8');
const rectangles = stdin.trim('\n').split('\n');

rectangles.forEach((rectangle) => {
  const [H, W] = rectangle.split(' ').map(Number);

  if (H === 0 || W === 0) return;

  for (let h = 0; h < H; h++) {
    var line = '';

    for (let w = 0; w < W; w++) {
      line = line + '#';
    }

    console.log(line);
  }

  console.log();
});
