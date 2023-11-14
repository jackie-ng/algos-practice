class Solution:
    def rob(self, nums: List[int]) -> int:
        
        ### Top Down ###
        def top_down(i):
            # no more houses left
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            optimal_profit = max(top_down(i + 1), top_down(i + 2) + nums[i])
            memo[i] = optimal_profit
            return optimal_profit
        memo = {}
        return top_down(0)
        
        ### Bottom Up ###
#         rob1, rob2 = 0, 0
        
#         # [rob1, rob2, n, n+1,...]
#         for n in nums:
#             rob1, rob2 = rob2, max(rob1+n,rob2)
#         return rob2