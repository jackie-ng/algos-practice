class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # Memoization dictionary to store results of subproblems
        memo = {}

        def recursivePaths(i, j):
            # Check if the result is already memoized
            if (i, j) in memo:
                return memo[(i, j)]

            # Check if the current cell is an obstacle
            if obstacleGrid[i][j] == 1:
                return 0

            # Base case: if at the bottom-right corner, there's only one way
            if i == m - 1 and j == n - 1:
                return 1

            # Explore two choices: move right or move down
            paths_right = recursivePaths(i, j + 1) if j + 1 < n else 0
            paths_down = recursivePaths(i + 1, j) if i + 1 < m else 0

            # Calculate the total number of unique paths
            total_paths = paths_right + paths_down

            # Memoize the result before returning
            memo[(i, j)] = total_paths
            return total_paths

        # Start the recursive process with initial indices (0, 0)
        return recursivePaths(0, 0)