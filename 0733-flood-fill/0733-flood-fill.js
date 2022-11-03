/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */

/*
Input: image = [[1,1,1],
                [1,1,0],
                [1,0,1]],
        sr = 1, sc = 1, color = 2
Output: [[2,2,2],
         [2,2,0],
         [2,0,1]]
*/
/**************BFS*******************/
function floodFill(image, r, c, replacement) {
    const currColor = image[r][c];
    if (currColor === replacement) return image;
    const queue = [[r, c]];
    
    while (queue.length) {
        const [row, col] = queue.shift();
        const deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        
        if (image[row][col] === currColor){
            image[row][col] = replacement;
            if(row-1 >= 0) queue.push([row-1, col]);  //up
            if(row+1 < image.length) queue.push([row+1, col]);  //down
            if(col+1 < image[0].length) queue.push([row, col+1]);  //right
            if(col-1 >= 0) queue.push([row, col-1]);  //left   
        }
    }
   return image;
}