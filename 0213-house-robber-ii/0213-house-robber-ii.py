class Solution:
    def rob(self, nums: List[int]) -> int:
        # reuse house robber I function
        def house_robber(nums):
            rob1, rob2 = 0, 0
            
            for n in nums:
                rob1, rob2 = rob2, max(rob1 + n, rob2)
            return rob2
        # nums[0] for edge case, skip nums[0], skip nums[-1]
        return max(nums[0], house_robber(nums[1:]), house_robber(nums[:-1]))