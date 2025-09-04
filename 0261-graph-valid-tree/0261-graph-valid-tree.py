class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Must have exactly n-1 edges
        if len(edges) > (n - 1):
            return False
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        seen = set()
        ## Recusive
        # def dfs(node, parent):
        #     if node in seen:
        #         return False
            
        #     seen.add(node)
        #     for nei in adj[node]:
        #         if nei == parent:
        #             continue # ignore the edge back to parent
        #         if not dfs(nei, node):
        #             return False
        #     return True
        # # Start from 0 (if n >= 1)
        # dfs(0, -1)

        ## Iterative
        stack = [(0, -1)]  # (node, parent)

        while stack:
            u, parent = stack.pop()
            if u in seen:
                continue
            seen.add(u)
            for v in adj[u]:
                if v == parent:
                    continue
                if v not in seen:
                    stack.append((v, u))
        # Connected if we visited all nodes
        return len(seen) == n