class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m, n = len(obstacleGrid), len(obstacleGrid[0])

#         # Memoization dictionary to store results of subproblems
#         memo = {}

#         def recursivePaths(i, j):
#             # Check if the result is already memoized
#             if (i, j) in memo:
#                 return memo[(i, j)]

#             # Check if the current cell is an obstacle
#             if obstacleGrid[i][j] == 1:
#                 return 0

#             # Base case: if at the bottom-right corner, there's only one way
#             if i == m - 1 and j == n - 1:
#                 return 1

#             # Explore two choices: move right or move down
#             paths_right = recursivePaths(i, j + 1) if j + 1 < n else 0
#             paths_down = recursivePaths(i + 1, j) if i + 1 < m else 0

#             # Calculate the total number of unique paths
#             total_paths = paths_right + paths_down

#             # Memoize the result before returning
#             memo[(i, j)] = total_paths
#             return total_paths

#         # Start the recursive process with initial indices (0, 0)
#         return recursivePaths(0, 0)
            m, n = len(obstacleGrid), len(obstacleGrid[0])

            # Create a 2D DP array to store the number of unique paths
            dp = [[0] * n for _ in range(m)]

            # Initialize the DP array for the top-left corner
            dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

            # Initialize the DP array for the first row
            for i in range(1, m):
                dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0

            # Initialize the DP array for the first column
            for j in range(1, n):
                dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0

            # Update the DP array for the rest of the grid
            for i in range(1, m):
                for j in range(1, n):
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

            return dp[-1][-1]
