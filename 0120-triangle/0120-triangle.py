class Solution:
    def minimumTotalMemo(self, triangle: List[List[int]]) -> int:
        n = len(triangle)  # Get the number of rows (n) in the triangle

        # Initialize a memoization dictionary to store minimum sums for subproblems
        memo = {}

        def dfs(row, col):
            """
            Recursive helper function to calculate the minimum path sum from a specific cell.

            Args:
              row: The row index (0-based) of the current cell.
              col: The column index (0-based) of the current cell.

            Returns:
              The minimum path sum from the current cell to the bottom of the triangle.
            """

            if row == n - 1:  # Base case: Reached the bottom row, return the value
                return triangle[row][col]

            # Check if the minimum sum for this cell has already been calculated
            if (row, col) in memo:
                return memo[(row, col)]

            # Explore both paths (down-left and down-right) recursively
            down_left = dfs(row + 1, col) + triangle[row][col]
            down_right = dfs(row + 1, col + 1) + triangle[row][col]

            # Store the minimum sum for this cell in the memo dictionary
            memo[(row, col)] = min(down_left, down_right)
            return memo[(row, col)]

        # Start the recursion from the top cell (row 0, col 0)
        return dfs(0, 0)
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Calculates the minimum path sum from top to bottom in the given triangle using DP tabulation.

        Args:
          triangle: A 2D list representing the triangle, where each row is a list of integers.

        Returns:
          The minimum path sum from top to bottom.
        """

        n = len(triangle)  # Get the number of rows (n) in the triangle

        # DP table to store minimum sums for reaching each row
        dp = [float('inf')] * (n + 1)  # Extra row to handle edge cases

        # Base case: Last row elements are their own minimum sums (avoiding out-of-bounds)
        for i in range(n):
            dp[i] = triangle[n - 1][i]

        # Iterate from bottom-up (excluding the last row)
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Minimum sum to reach the current cell from the row below
                dp[col] = min(dp[col], dp[col + 1]) + triangle[row][col]

        # Minimum sum for the entire path starts from the top cell (row 0)
        return dp[0]