class Solution:
    def minDistanceMemo(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i < 0 and j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i < 0:
                memo[(i, j)] = 1 + dfs(i, j-1)
                return memo[(i, j)]
            if j < 0:
                memo[(i, j)] = 1 + dfs(i-1, j)
                return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i-1, j-1)
            else:
                memo[(i, j)] = min(1+dfs(i, j-1), 1+dfs(i-1, j))
            return memo[(i, j)]
        return dfs(len(word1) - 1, len(word2) - 1)
    
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            dp[i][0] = 1 + dp[i-1][0]
        for i in range(1, n+1):
            dp[0][i] = 1 + dp[0][i-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(1+dp[i-1][j], 1+dp[i][j-1])
        return dp[m][n]
        
        