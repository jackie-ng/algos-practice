/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countComponents = function(n, edges) {
    //convert to an adjacency list
    const graph = buildGraph(n, edges);
    let res = 0;
    let visited = []
    for (let i = 0; i < n; i++) {
        visited.push(false);
    }
    //traverse graph
    for (let i = 0; i < n; i++) {
        if (visited[i] === false) {
            res++;
            dfs(i, graph, visited);
        }
    }
    return res;
};

const buildGraph = (n, edges) => {
    let graph = Array.from({length: n}, () => []);
    for (let edge of edges) {
        let [src, dst] = edge;
        graph[src].push(dst);
        graph[dst].push(src);
    }
    return graph;
}

const dfs = (index, graph, visited) => {
    visited[index] = true;
    let node = graph[index];
    for (let i = 0; i < node.length; i++) {
        let cur = node[i];
        if (visited[cur] === false) {
            dfs(cur, graph, visited)
        }
    }
}