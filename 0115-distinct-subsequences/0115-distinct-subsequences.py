class Solution:
        def numDistinct(self, s: str, t: str) -> int:
#             # Dictionary for memoization
#             memo = {}

#             def dfs(i, j):

#                 # Base case: checks if either i has reached the end of s, j has reached the end of t, 
#                 # or the remaining length of s is less than the remaining length of t. 
#                 if i == len(s) or j == len(t) or len(s) - i < len(t) - j:
#                     return int(j == len(t))

#                 # Check if the result is already cached
#                 if (i, j) in memo:
#                     return memo[i,j]

#                 # Always make this recursive call
#                 res = dfs(i + 1, j)
                
#                 # If the characters match, add the result to "res"
#                 # continuing checking
#                 if s[i] == t[j]:
#                     res += dfs(i + 1, j + 1)

#                 # Cache the answer and return
#                 memo[i, j] = res
#                 return res                

#             return dfs(0, 0)
    
#         M, N = len(s), len(t)
        
#         # Dynamic Programming table
#         dp = [[0 for i in range(N + 1)] for j in range(M + 1)] 
        
#         # Base case initialization
#         for j in range(N + 1):
#             dp[M][j] = 0
        
#         # Base case initialization
#         for i in range(M + 1):
#             dp[i][N] = 1
        
#         # Iterate over the strings in reverse so as to
#         # satisfy the way we've modeled our recursive solution
#         for i in range(M - 1, -1, -1):
#             for j in range(N - 1, -1, -1):
          
#                 # Remember, we always need this result
#                 dp[i][j] = dp[i + 1][j]

#                 # If the characters match, we add the
#                 # result of the next recursion call (in this
#                 # case, the value of a cell in the dp table
#                 if s[i] == t[j]:
#                     dp[i][j] += dp[i + 1][j + 1]
            
#         return dp[0][0]
    
            m = len(s)
            n = len(t)
            # Dynamic Programming table
            dp = [[0] * (n+1) for _ in range(m+1)]

            # Base case initialization
            for i in range(m+1):
                dp[i][0] = 1

            """redundant, as we have initialised dp table with full of zeros"""
    #         for i in range(1, n+1): 
    #             dp[0][i] = 0

            for i in range(1, m+1):
                for j in range(1, n+1):
                    dp[i][j] += dp[i-1][j] 			#if current character is skipped
                    if s[i-1] == t[j-1]:
                        dp[i][j] += dp[i-1][j-1]	#if current character is used

            return dp[-1][-1]