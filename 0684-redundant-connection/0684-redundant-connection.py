class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                # parent[p] = parent[parent[p]] # path compression: set p parent to its grandparent to shorten the path as we go up to the path
                p = parent[p] # while p is not equal to its own parent, keep going up the length
            return p # once we got into the root parent => return parent[n]

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2) # find the root parent first

            if p1 == p2:
                return False 
            if rank[p1] > rank[p2]: # p1 is the parent of p2
                parent[p2] = p1
                rank[p1] += rank[p2]
            else: # p2 is the parent of p1
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
