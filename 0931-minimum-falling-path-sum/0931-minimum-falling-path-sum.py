class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}
        def dfs(row, col):
            # check if out of bound
            if 0 > row or row >= n or 0 > col or col >= n:
                return float('inf')
            # Base case: Reached the last row (no more downward movement)
            if row == n-1:
                return matrix[row][col]
            
            # check if already in the memo
            if (row, col) in memo:
                return memo[(row, col)]  # Use the memoized result if available
            # traverse down, down_left, down_right
            down = matrix[row][col] + dfs(row+1, col)
            down_left = matrix[row][col] + dfs(row+1, col-1)
            down_right = matrix[row][col] + dfs(row+1, col+1)
            # Store the minimum sum in the memo
            memo[(row, col)] = min(down, down_left, down_right)
            # return the minimum sum for this starting position
            return memo[(row, col)]
        # try recursion for each element in the first row
        min_sum = float('inf')
        for col in range(n):
            min_sum = min(min_sum, dfs(0, col))
            
        return min_sum