class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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
        