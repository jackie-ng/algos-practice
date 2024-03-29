/**Write a function, prereqsPossible, that takes in a number of courses (n) and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of [A, B] means that course A must be taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses. */
const prereqsPossible = (numCourses, prereqs) => {
  const visiting = new Set();
  const visited = new Set();

  const graph = buildGraph(numCourses, prereqs);
  for (let node in graph) {
    if (hasCycle(graph, node, visiting, visited)) {
      return false;
    }
  }

  return true;
};

const hasCycle = (graph, node, visiting, visited) => {
  if (visited.has(node)) return false;

  if (visiting.has(node)) return true;

  visiting.add(node);

  for (let neighbor of graph[node]) {
    if (hasCycle(graph, neighbor, visiting, visited)) {
      return true;
    }
  }

  visiting.delete(node);
  visited.add(node);

  return false;
};

const buildGraph = (numCourses, prereqs) => {
  const graph = {};

  for (let i = 0; i < numCourses; i += 1) {
    graph[i] = [];
  }

  for (let prereq of prereqs) {
    const [a, b] = prereq;
    graph[a].push(String(b));
  }

  return graph;
};
// p = # prereqs
// n = # courses
// Time: O(n + p)
// Space: O(n)

/**test_00:
const numCourses = 6;
const prereqs = [
  [0, 1],
  [2, 3],
  [0, 2],
  [1, 3],
  [4, 5],
];
prereqsPossible(numCourses, prereqs); // -> true
test_01:
const numCourses = 6;
const prereqs = [
  [0, 1],
  [2, 3],
  [0, 2],
  [1, 3],
  [4, 5],
  [3, 0],
];
prereqsPossible(numCourses, prereqs); // -> false
test_02:
const numCourses = 5;
const prereqs = [
  [2, 4],
  [1, 0],
  [0, 2],
  [0, 4],
];
prereqsPossible(numCourses, prereqs); // -> true
test_03:
const numCourses = 6;
const prereqs = [
  [2, 4],
  [1, 0],
  [0, 2],
  [0, 4],
  [5, 3],
  [3, 5],
];
prereqsPossible(numCourses, prereqs); // -> false */
