class Solution:
    def uniquePathsMemo(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m-1 or j == n-1:
                return 1
            right = dfs(i, j+1) if j+1 < n else 0
            left = dfs(i+1, j) if i+1 < m else 0
            total = right + left
            memo[(i, j)] = total
            return total
        return dfs(0,0)
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]