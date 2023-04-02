const stdin = require('fs').readFileSync(0, 'utf-8');
const boards = stdin.trim('\n').split('\n');

boards.forEach((board) => {
  const [H, W] = board.split(' ').map(Number);

  if (H === 0 || W === 0) return;

  for (let h = 0; h < H; h++) {
    var line = '';

    for (let w = 0; w < W; w++) {
      if ((h % 2 && w % 2) || !(h % 2) && !(w % 2)) {
        line = line + '#';
      } else {
        line = line + '.';
      }
    }

    console.log(line);
  }

  console.log();
});
