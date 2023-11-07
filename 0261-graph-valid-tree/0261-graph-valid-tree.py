# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         if not n:
#             return True
        
#         adj = { i:[] for i in range(n) }
#         for n1, n2 in edges:
#             adj[n1].append(n2)
#             adj[n2].append(n1)
            
#         visit = set()
#         def dfs(i, prev):
#             if i in visit: # detect a loop
#                 return False
            
#             visit.add(i)
            
#             for j in adj[i]:
#                 if j == prev:
#                     continue
#                 if not dfs(j, i):
#                     return False
#             return True
        
#         return dfs(0, -1) and n == len(visit)
                
# alternative solution via DSU O(ElogV) time complexity and 
# save some space as we don't recreate graph\tree into adjacency list prior dfs and loop over the edge list directly

            
    
class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n - 1: return False
        
        root = [i for i in range(n)]
        rank = [1] * n
        count = n
    
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            nonlocal count
            rootX = find(x)
            rootY = find(y)
            # if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                root[rootY] = rootX 
            elif rank[rootY] > rank[rootX]:
                root[rootX] = rootY
            else:
                root[rootY] = rootX
                rank[rootX] += 1
            count -= 1


        # Add each edge. Check if a merge happened, because if it 
        # didn't, there must be a cycle.
        for e1, e2 in edges:
            if find(e1) == find(e2):
                return False
            union(e1, e2)
        # If we got this far, there's no cycles!
        return count == 1
