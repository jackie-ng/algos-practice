/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    let result = [];
    
    function dfs(root, cur) {
        if (!root) return;
        if (!root.left && !root.right) {
            result.push(cur + root.val);
            return;
        }
        dfs(root.left, cur + root.val + "->")
        dfs(root.right, cur + root.val + "->")
    }
    dfs(root, "");
    
    return result;
    
};