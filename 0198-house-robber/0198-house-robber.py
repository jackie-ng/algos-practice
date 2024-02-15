class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # ### Top Down ###
        # def top_down(i):
        #     if i >= len(nums):
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = max(top_down(i + 1), top_down(i + 2) + nums[i]) # optimal_profit
        #     return memo[i]
        # memo = {}
        # return top_down(0)
        ### Bottom Up ###
#         rob1, rob2 = 0, 0
#         # [rob1, rob2, n, n+1,...]
#         for n in nums:
#             rob1, rob2 = rob2, max(rob1+n,rob2)
#         return rob2

        if len(nums) == 1:
            return nums[0]
        
        dp = [None] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            print(dp)
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return max(dp)