class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Dictionary for memoization
        memo = {}
        
        def uniqueSubsequences(i, j):
            
            M, N = len(s), len(t)
            
            # Base case
            if i == M or j == N or M - i < N - j:
                return int(j == len(t))
            
            # Check if the result is already cached
            if (i, j) in memo:
                return memo[i,j]
            
            # Always make this recursive call
            ans = uniqueSubsequences(i + 1, j)
            
            # If the characters match, make the other
            # one and add the result to "ans"
            if s[i] == t[j]:
                ans += uniqueSubsequences(i + 1, j + 1)
            
            # Cache the answer and return
            memo[i, j] = ans
            return ans                
        
        return uniqueSubsequences(0, 0)
    
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