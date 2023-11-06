class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]

        # return False if already unioned
        def union(n1, n2):
            r1, r2 = find(n1), find(n2) # find the root parent first

            if r1 == r2:
                return False 
            if rank[r1] > rank[r2]: # p1 is the parent of p2
                parent[r2] = r1
                # rank[p1] += rank[p2]
            else: # p2 is the parent of p1
                parent[r1] = r2
                rank[r2] += 1
                # rank[p2] += rank[p1]
                
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
