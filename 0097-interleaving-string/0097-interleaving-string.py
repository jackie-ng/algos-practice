class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        # If the lengths of s1 and s2 don't add up to the length of s3, it's impossible to form s3
        if len(s1) + len(s2) != len(s3):
            return False        
        # Initialize a 2D table to store intermediate results
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        # Base case: empty strings can always interleave to form an empty string
        dp[0][0] = True
    
        # Fill the first row (s1) and the first column (s2)
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        # Fill the rest of the table
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                # Check if s1 contributes to the current position
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) # Check if s2 contributes to the current position

        # The result is found at the bottom-right corner of the table
        return dp[len_s1][len_s2]

#         memo = {}
#         if len(s1) == 0:
#             return s2 == s3
#         if len(s2) == 0:
#             return s1 == s3
#         if len(s1) + len(s2) != len(s3): 
#             return False
        
#         def dfs(i,j):
#             if (i,j) in memo: 
#                 return memo[(i,j)]
            
#             c1 = c2 = False 
            
#             # Base case: If we have reached the end of all strings
#             if i == len(s1) and j == len(s2): 
#                 return True
                
#             # Check if interleaving is possible and recurse accordingly
#             if i < len(s1) and s1[i] == s3[i+j]:
#                 c1 = dfs(i+1,j)
           
#             if j < len(s2) and s2[j] == s3[i+j]:
#                 c2 = dfs(i,j+1)  
                
#             # Memoize the result before returning
#             memo[(i,j)] = c1 or c2
#             return c1 or c2
#         # Start the recursive process with initial indices (0, 0, 0)
#         dfs(0,0)
#         return memo[(0,0)]
        