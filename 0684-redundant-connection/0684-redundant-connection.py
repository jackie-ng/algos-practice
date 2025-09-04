class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        redundant = None
        # key - a set
        # key2 - a set2
        # Recursive
        def has_path(source, target, seen):
            if source == target:
                return True
            seen.add(source)
            for nei in graph[source]:
                #if the node hasn't been visited and there's a path to target 
                if nei not in seen and has_path(nei, target, seen):
                    return True
            return False
        # # Iterative
        # def has_path(src, dst):
        #     if src == dst:
        #         return True
        #     stack = [src]
        #     seen = {src}
        #     while stack:
        #         node = stack.pop()
        #         if node == dst:
        #             return True
        #         for nei in graph[node]:
        #             if nei not in seen:
        #                 seen.add(nei)
        #                 stack.append(nei)
        #     return False
        for u, v in edges:
            # Before adding u-v, check if path exists → would form a cycle
            if u in graph and v in graph and has_path(u, v, set()):
                redundant = [u, v]
            # Add edge to continue building full graph
            graph[u].append(v)
            graph[v].append(u)
        return redundant