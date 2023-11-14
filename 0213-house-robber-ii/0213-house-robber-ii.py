class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def house_robber(nums):
            rob1, rob2 = 0, 0
            
            for n in nums:
                rob1, rob2 = rob2, max(rob1 + n, rob2)
            return rob2
        
        return max(nums[0], house_robber(nums[1:]), house_robber(nums[:-1]))