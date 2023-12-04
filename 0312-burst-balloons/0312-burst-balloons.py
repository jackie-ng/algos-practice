class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        nums = [1] + nums + [1]
        def dfs(l, r):
            if l>r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            memo[(l,r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                memo[(l,r)] = max(memo[(l,r)], coins)
            return memo[(l,r)]
        return dfs(1, len(nums)-2)
    
#         A, n = [1] + A + [1], len(A) + 2
#         dp = [[0] * n for _ in range(n)]
        
#         for i in range(n - 2, -1, -1):
#             for j in range(i + 2, n):
#                 dp[i][j] = max(A[i]*A[k]*A[j] + dp[i][k] + dp[k][j] for k in range(i + 1, j))
        
#         return dp[0][n-1]