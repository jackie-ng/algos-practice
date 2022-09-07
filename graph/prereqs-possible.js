/**Write a function, hasCycle, that takes in an object representing the adjacency list of a directed graph. The function should return a boolean indicating whether or not the graph contains a cycle. */
const hasCycle = (graph) => {
  const visited = new Set();
  for (let startNode in graph) {
    if (cycleDetect(graph, startNode, new Set(), visited)) return true;
  }
  return false;
};

const cycleDetect = (graph, node, visiting, visited) => {
  if (visited.has(node)) return false;

  if (visiting.has(node)) return true;

  visiting.add(node);

  for (let neighbor of graph[node]) {
    if (cycleDetect(graph, neighbor, visiting, visited)) return true;
  }

  visiting.delete(node);
  visited.add(node);
  return false;
};

/**
n = number of nodes
Time: O(n^2)
Space: O(n)
 */

/**test_00:
hasCycle({
  a: ["b"],
  b: ["c"],
  c: ["a"],
}); // -> true
test_01:
hasCycle({
  a: ["b", "c"],
  b: ["c"],
  c: ["d"],
  d: [],
}); // -> false
test_02:
hasCycle({
  a: ["b", "c"],
  b: [],
  c: [],
  e: ["f"],
  f: ["e"],
}); // -> true
test_03:
hasCycle({
  q: ["r", "s"],
  r: ["t", "u"],
  s: [],
  t: [],
  u: [],
  v: ["w"],
  w: [],
  x: ["w"],
}); // -> false */
