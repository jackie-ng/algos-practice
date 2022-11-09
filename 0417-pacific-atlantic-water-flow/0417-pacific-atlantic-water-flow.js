/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
function pacificAtlantic(matrix) {
  if (!matrix.length) {
    return [];
  }
  let pacific = make(matrix);
  let atlantic = make(matrix);
    
  for (let row = 0; row < matrix.length; row++) {
    bfs(row, 0, pacific, matrix);
    bfs(row, matrix[0].length - 1, atlantic, matrix);
  }
  for (let col = 0; col < matrix[0].length; col++) {
    bfs(0, col, pacific, matrix);
    bfs(matrix.length - 1, col, atlantic, matrix);
  }
    let union = (atlantic, pacific) => {
      let union = [];
      for (let i = 0; i < atlantic.length; i++) {
        for (let j = 0; j < atlantic[0].length; j++) {
          if (atlantic[i][j] && pacific[i][j]) {
            union.push([i, j]);
          }
        }
      }
      return union;
    }
  return union(atlantic, pacific);
};

const make = matrix => new Array(matrix.length).fill().map(row => new Array(matrix[0].length).fill(false));

function bfs(x, y, ocean, matrix) {
  let q = [[x, y]];
  ocean[x][y] = true;
  while (q.length) {
    let [i, j] = q.shift();
    for (let [newI, newJ] of [[i , j+1], [i+1, j], [i, j-1], [i-1, j]]) {
      if (newI >= 0 && newI < ocean.length && newJ >= 0 && newJ < ocean[0].length) {
        if (matrix[i][j] <= matrix[newI][newJ] && !ocean[newI][newJ]) {
          q.push([newI, newJ]);
          ocean[newI][newJ] = true;
        }
      }
    } 
  }
}

