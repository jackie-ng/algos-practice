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
        return dp[-1][-1]


#         if len(s1) + len(s2) != len(s3):
#             return False
        
#         def dfs(i,j):
#          # Bottom Up approach This is the goal state
#             if i == len(s1) and j == len(s2):
#                 return True 
#             # using memo
#             if (i,j) in memo:
#                 return memo[(i,j)]

#             if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1,j) : # Checking if we take the s1 substring 
#                 memo[(i,j)] = True
#                 return True
#             if j < len(s2) and s2[j] == s3[i+j] and dfs(i,j+1) : # Checking if we take the s2 substring
#                 memo[(i,j)] = True
#                 return True
#             memo[(i,j)] = False                                                       
            
#             return False


#         memo = {} #memo : [(i,j)] = True or False, need to only mark false nodes
#         # while i <= len(s1) and j <=len(s2) and i+j len(s3):          
#         return dfs(0,0)