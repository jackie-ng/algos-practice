/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
/*
Input: mat = [[0,0,0],
              [0,1,0],
              [1,1,1]]
Output:      [[0,0,0],
              [0,1,0],
              [1,2,1]]
*/

const updateMatrix = mat => {
  const queue = [];
  for (let row = 0; row < mat.length; row++) {
    for (let col = 0; col < mat[0].length; col++) {
      if (!mat[row][col]) queue.push([row, col, 0]);
      else mat[row][col] = Infinity;
    }
  }
  
  const dir = [[0,1], [1,0], [-1,0], [0,-1]];
  const endR = mat.length - 1, endC = mat[0].length - 1;
  
  while (queue.length) {
    const [curR, curC, distance] = queue.shift();
    if (mat[curR][curC] > distance) mat[curR][curC] = distance;
    for (let [addR, addC] of dir) {
      const [newR, newC] = [curR + addR, curC + addC];
      if (newR < 0 || newC < 0 || newR > endR || newC > endC) continue;
      if (mat[newR][newC] === Infinity) queue.push([newR, newC, distance + 1])
    }
  }
  
  return mat;
};