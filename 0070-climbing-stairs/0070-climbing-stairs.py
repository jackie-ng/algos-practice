class Solution:
    def climbStairsMemo(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i <= 2:
                return i
            if i not in memo:
                memo[i] = dfs(i-1) + dfs(i-2)
            return memo[i]
        return dfs(n)
    
    def climbStairsBU(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        # Base case
        one = 1
        two = 2
        
        for i in range(3, n + 1):
            one, two = two, one + two
        
        return two