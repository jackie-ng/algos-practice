class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            if root[n] != n:
                root[n] = find(root[n])
            return root[n]

        # return False if already unioned
        def union(n1, n2):
            r1, r2 = find(n1), find(n2) # find the root parent first

            if r1 == r2:
                return False 
            if rank[r1] > rank[r2]: # r1 is the parent of r2
                root[r2] = r1
            else: # r2 is the parent of r1
                root[r1] = r2
                rank[r2] += 1
                
            return True

        for n1, n2 in edges:
            # print(n1, n2, "root", root, "rank", rank)
            if not union(n1, n2):
                return [n1, n2]
