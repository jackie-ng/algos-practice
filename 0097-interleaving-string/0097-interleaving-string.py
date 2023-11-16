class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        # If the lengths of s1 and s2 don't add up to the length of s3, it's impossible to form s3
        if len_s1 + len_s2 != len_s3:
            return False        
        # Initialize a 2D table to store intermediate results
        dp = [[False] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        
        # Base case: empty strings can always interleave to form an empty string
        dp[0][0] = True
    
        # Fill the first row (s1) and the first column (s2)
        for i in range(1, len_s1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, len_s2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        # Fill the rest of the table
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                # Check if s1 contributes to the current position
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) # Check if s2 contributes to the current position

        # The result is found at the bottom-right corner of the table
        return dp[len_s1][len_s2]

#         # Memoization dictionary to store results of subproblems
#         memo = {}

#         def recursiveInterleave(i, j, k):
#             # Check if the result is already memoized
#             if (i, j, k) in memo:
#                 return memo[(i, j, k)]

#             # Base case: If we have reached the end of all strings
#             if i == len(s1) and j == len(s2) and k == len(s3):
#                 return True

#             # Check if interleaving is possible and recurse accordingly
#             result = (
#                 (i < len(s1) and s1[i] == s3[k] and recursiveInterleave(i + 1, j, k + 1)) or
#                 (j < len(s2) and s2[j] == s3[k] and recursiveInterleave(i, j + 1, k + 1))
#             )

#             # Memoize the result before returning
#             memo[(i, j, k)] = result
#             return result

#         # Start the recursive process with initial indices (0, 0, 0)
#         return recursiveInterleave(0, 0, 0)
        