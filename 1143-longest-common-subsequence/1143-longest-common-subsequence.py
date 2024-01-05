class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
#         # Make a grid of 0's with len(text2) + 1 columns 
#         # and len(text1) + 1 rows.
#         dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
#         # Iterate up each column, starting from the last one.
#         for col in reversed(range(len(text2))):
#             for row in reversed(range(len(text1))):
#                 # If the corresponding characters for this cell are the same...
#                 if text2[col] == text1[row]:
#                     dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
#                 # Otherwise they must be different...
#                 else:
#                     dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        
#         # The original problem's answer is in dp_grid[0][0]. Return it.
#         return dp_grid[0][0]
    
        
#         dp = [[0] *(len(text2)+1) for _ in range(len(text1)+1)]
#         for i in range(len(text1)):
#             for j in range(len(text2)):
#                 if text1[i] == text2[j]:
#                     dp[i+1][j+1] = 1 + dp[i][j]
#                 else:
#                     dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                    
#         return dp[-1][-1]
    
    
        #### We can save a lot of space by instead of keeping track of an entire 2D array, 
        #### only keeping track of the last two columns.
        
        # Make sure text1 is shorter than text 2
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        
        # The previous column starts with all 0's and like before is 1
        # more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        
        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            # Create a new array to represent the current column.
            current = [0] * (len(text1) + 1)
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one.
            previous = current
        
        # The original problem's answer is in previous[0]. Return it.
        return previous[0]

