class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list for 0..n-1
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen = set()
        components = 0
        # # Recursive
        # def dfs(u):
        #     seen.add(u)
        #     for v in graph[u]:
        #         if v not in seen:
        #             dfs(v)
        # for node in range(n):
        #     if node not in seen:
        #         components += 1
        #         dfs(node)
        # Iterative
        for start in range(n):
            if start in seen:
                continue
            components += 1
            # Explicit stack simulating recursion
            stack = [start]
            seen.add(start)
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
        return components