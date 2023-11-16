class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#         # Memoization dictionary to store results of subproblems
#         memo = {}

#         def recursivePaths(i, j):
#             # Check if the result is already memoized
#             if (i, j) in memo:
#                 return memo[(i, j)]

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

            # Create a 2D table to store the number of unique paths
            dp = [[0] * n for _ in range(m)]

            # Initialize the first row and first column with 1, as there is only one way to reach each position
            for i in range(m):
                dp[i][0] = 1

            for j in range(n):
                dp[0][j] = 1

            # Fill the table iteratively
            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

            # The bottom-right corner contains the total number of unique paths
            return dp[m - 1][n - 1]