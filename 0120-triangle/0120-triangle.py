class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
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