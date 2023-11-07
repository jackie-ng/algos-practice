class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0:
            return 0
        
        n = len(isConnected)
        root = [i for i in range(n)]
        rank = [1] * n
        count = n
        
        
        def find(n):
            if root[n] != n:
                root[n] = find(root[n])
            return root[n]
            
        def union(n1, n2):
            nonlocal count
            r1, r2 = find(n1), find(n2)
            
            if r1 != r2:
                if rank[r1] > rank[r2]:
                    root[r2] = r1
                elif rank[r2] > rank[r1]:
                    root[r1] = r2
                else:
                    root[r1] = r2
                    rank[r2] += 1
                count -= 1
        
        for row in range(n):
            for col in range(n):            
                if isConnected[row][col] == 1:
                    union(row, col)
        return count