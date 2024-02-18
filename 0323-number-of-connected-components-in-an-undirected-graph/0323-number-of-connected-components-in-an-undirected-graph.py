class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n)]
        rank = [1] * n
        res = n
        
        def find(n):
            if root[n] != n:
                root[n] = find(root[n])
            return root[n]
            
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            # if r1 and r2 trees are in the same component
            if r1 == r2:
                return 0
            if rank[r1] > rank[r2]:
                root[r2] = r1
            elif rank[r2] > rank[r1]:
                root[r1] = r2
            else:
                root[r1] = r2
                rank[r2] += 1
            
            # if r1 and r2 trees are in the different components
            return 1
        
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
        