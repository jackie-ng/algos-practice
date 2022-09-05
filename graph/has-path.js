/**Write a function, hasPath, that takes in an object representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes. */

/**dfs */

const hasPath = (graph, src, dst) => {
  if (src === dst) return true;

  for (let neighbor of graph[src]) {
    if (hasPath(graph, neighbor, dst) === true) {
      return true;
    }
  }

  return false;
};
/*
n = number of nodes
e = number edges
Time: O(e)
Space: O(n)*/


/**bfs */
const hasPath = (graph, src, dst) => {
  const queue = [src];

  while (queue.length) {
    const current = queue.shift();
    if (current === dst) return true;

    for (let neighbor of graph[current]) {
      queue.push(neighbor);
    }
  }

  return false;
};

/**
n = number of nodes
e = number edges
Time: O(e)
Space: O(n) */
/**const graph = {
  f: ['g', 'i'],
  g: ['h'],
  h: [],
  i: ['g', 'k'],
  j: ['i'],
  k: []
};

hasPath(graph, 'f', 'k'); // true */

/**const graph = {
  f: ['g', 'i'],
  g: ['h'],
  h: [],
  i: ['g', 'k'],
  j: ['i'],
  k: []
};

hasPath(graph, 'f', 'j'); // false */

/**const graph = {
  v: ['x', 'w'],
  w: [],
  x: [],
  y: ['z'],
  z: [],
};

hasPath(graph, 'v', 'w'); // true */

/**const graph = {
  v: ['x', 'w'],
  w: [],
  x: [],
  y: ['z'],
  z: [],
};

hasPath(graph, 'v', 'z'); // false */
