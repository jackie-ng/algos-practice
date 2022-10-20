/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countComponents = function(n, edges) {
    
    let count = 0;
    let visited = new Set();
    const graph = buildGraph(n, edges);
    for (let i = 0; i < n; i++) {
        console.log(i)
        if (explore(graph, i, visited) === true) {
            count += 1;
        }
    }

    return count;
};


const buildGraph = (n, edges) => {
let graph = Array.from({length: n}, () => []);
    
    for (let [src, dist] of edges) {
        graph[src].push(dist);
        graph[dist].push(src);
    }
    return graph
}
const explore = (graph, current, visited) => {
  if (visited.has(String(current))) return false;
  visited.add(String(current))
  //console.log(graph[current])
  for (let neighbor of graph[current]) {
    explore(graph, neighbor, visited);
  }
  return true;
}
