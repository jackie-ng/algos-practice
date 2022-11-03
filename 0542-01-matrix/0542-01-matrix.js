/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function(matrix) {
    let queue = [];
    for (let r = 0; r < matrix.length; r++) {
        for (let c = 0; c < matrix[0].length; c++) {
            if (matrix[r][c] === 0) {
                queue.push([r, c, 0]);
            } else {
                matrix[r][c] = Infinity;
            }
        }
    }
    
    while (queue.length) {
        const [ curRow, curCol, distance ] = queue.shift();
        
        const deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        if (matrix[curRow][curCol] > distance) matrix[curRow][curCol] = distance;
        for (let delta of deltas) {
            const [addRow, addCol] = delta;
            const [newRow, newCol] = [curRow + addRow, curCol + addCol];
            
            const rowInbounds = 0 <= newRow && newRow < matrix.length;
            const colInbounds = 0 <= newCol && newCol < matrix[0].length;
            
            if (!rowInbounds || !colInbounds) continue;
            if (matrix[newRow][newCol] === Infinity) queue.push([newRow, newCol, distance+1])
        }        
    }
    return matrix;
};