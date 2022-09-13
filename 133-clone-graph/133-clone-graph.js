/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */

/*https://leetcode.com/problems/clone-graph/discuss/1416436/Javascript-DFS-%2B-Hashmap-(Thought-Process)*/

var cloneGraph = function(node, copy = new Map()) {
    // Handle null case
    if (!node) return null;
        
    // If our graph hasn't already copied the input node
    if (!copy.has(node.val)) {
        // Create new copy node (+ reference in map)
        copy.set(node.val, new Node(node.val));
        // Recursively clone neighbors
        copy.get(node.val).neighbors = node.neighbors.map((neighbor) => cloneGraph(neighbor, copy));
    }
        
    // Return copied/new node (* not * the original node passed in)
    return copy.get(node.val);
};