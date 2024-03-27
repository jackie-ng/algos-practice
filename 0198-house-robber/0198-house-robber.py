class Solution:
    def robMemo(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dfs(i+1), dfs(i+2) + nums[i])
            return memo[i]
        return dfs(0)
    
    def robBU(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [None] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return max(dp)
    
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for n in nums:
            rob1, rob2 = rob2, max(rob1+n, rob2)
        return rob2