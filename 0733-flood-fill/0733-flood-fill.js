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


/**************Recursion*************/
function floodFill(image, r, c, newColor, firstColor = image[r][c]) {
    //handle the coordinate out of bounds
    // or if it's already a new color
    // or it's not the original we're trying to change
    
    if (r < 0 || c < 0 || r >= image.length || c >= image[r].length
       || image[r][c] !== firstColor || image[r][c] === newColor) {
        return image //return image as it is
    }
    //reassigning image color
    image[r][c] = newColor
    //recursion 
    floodFill(image, r+1, c, newColor, firstColor);
    floodFill(image, r-1, c, newColor, firstColor);
    floodFill(image, r, c+1, newColor, firstColor);
    floodFill(image, r, c-1, newColor, firstColor);
    
    //return modified image
    return image;
    
}
/**************DFS*******************/
/**************BFS*******************/
// function floodFill(image, r, c, replacement) {
//     const currColor = image[r][c];
//     if (currColor === replacement) return image;
//     const queue = [[r, c]];
    
//     while (queue.length) {
//         const [row, col] = queue.shift();
//         const deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        
//         if (image[row][col] === currColor){
//             image[row][col] = replacement;
//             if(row-1 >= 0) queue.push([row-1, col]);  //up
//             if(row+1 < image.length) queue.push([row+1, col]);  //down
//             if(col+1 < image[0].length) queue.push([row, col+1]);  //right
//             if(col-1 >= 0) queue.push([row, col-1]);  //left   
//         }
//     }
//    return image;
// }