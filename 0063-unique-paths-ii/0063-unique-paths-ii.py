class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            right = dfs(i, j+1) if j+1 < n else 0 
            down = dfs(i+1, j) if i+1 < m else 0 
            total = right + down
            memo[(i, j)] = total
            return total
        return dfs(0,0)