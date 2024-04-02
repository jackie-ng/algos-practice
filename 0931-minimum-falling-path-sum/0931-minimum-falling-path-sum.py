class Solution:
    def minFallingPathSumMemo(self, matrix: List[List[int]]) -> int:
        """
        Calculates the minimum sum of any falling path through the given matrix using memoization.
        Args:
          matrix: A 2D list representing the matrix of integers.
        Returns:
          The minimum sum of any falling path from the first row to the bottom.
        """  
        n = len(matrix)
        memo = {}  # Dictionary to store memoized results (minimum sums for starting positions)

        def dfs(row, col):
            """
            Recursive helper function to find the minimum sum of a falling path starting from a cell.
            Args:
                row: The row index (0-based) of the current cell.
                col: The column index (0-based) of the current cell.
            Returns:
                The minimum sum of a falling path starting from the current cell.
            """
            # Check if the cell is outside the grid boundaries (invalid path)
            if 0 > row or row >= n or 0 > col or col >= n:
                return float('inf')  # Return positive infinity for invalid paths

            # Base case: Reached the last row (no more downward movement)
            if row == n - 1:
                return matrix[row][col]  # Return the value at the current cell

            # Check if the minimum sum for this starting position has already been calculated
            if (row, col) in memo:
                return memo[(row, col)]  # Use the memoized result if available

            # Explore all three possible downward directions (valid)
            down = matrix[row][col] + dfs(row + 1, col)  # Move directly down
            down_left = matrix[row][col] + dfs(row + 1, col - 1)  # Move diagonally left
            down_right = matrix[row][col] + dfs(row + 1, col + 1)  # Move diagonally right

            # Store the minimum sum for this starting position in the memo dictionary
            memo[(row, col)] = min(down, down_left, down_right)

            # Return the minimum sum for this starting position (considering all directions)
            return memo[(row, col)]

          # Start the recursion from each element in the first row
        min_sum = float('inf')
        for col in range(n):
            min_sum = min(min_sum, dfs(0, col))

        return min_sum
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Calculates the minimum sum of any falling path through the given matrix using DP tabulation.

        Args:
          matrix: A 2D list representing the n x n integer matrix.

        Returns:
          The minimum sum of any falling path through the matrix.
        """
        n = len(matrix)

        # Initialize a DP table to store minimum sums for each cell
        dp = [[float('inf')] * n for _ in range(n)]

        # Base case: First row elements are their own minimum sums
        for i in range(n):
            dp[0][i] = matrix[0][i]

        # Iterate through the matrix from row 1 onwards
        for row in range(1, n):
            for col in range(n):
                # Explore possible paths from the cell above
                up = dp[row - 1][col]
                left_diag = dp[row - 1][col - 1] if col > 0 else float('inf')
                right_diag = dp[row - 1][col + 1] if col < n - 1 else float('inf')

                # Update the minimum sum for the current cell
                dp[row][col] = min(up, left_diag, right_diag) + matrix[row][col]

        # Minimum sum for the entire path is the minimum in the last row
        return min(dp[-1])