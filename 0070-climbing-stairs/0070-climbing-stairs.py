class Solution:
    def climbStairs(self, n: int) -> int:
        # Top Down with Memoization
#         def dp(i):
#             if i <= 2:
#                 return i
#             # Instead of just returning dp(i - 1) + dp(i - 2), calculate it once and then
#             # store the result inside a hashmap to refer to in the future.
#             if i not in memo:
#                 memo[i] = dp(i - 1) + dp(i - 2)
#             return memo[i]
        
#         memo = {}
#         return dp(n)
        
        # Bottom Up
        if n == 1:
            return 1
        # An array that represents the answer to the problem for a given state
        dp = [0] * (n + 1)
        # Base case
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]