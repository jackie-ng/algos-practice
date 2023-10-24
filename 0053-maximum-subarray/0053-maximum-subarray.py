class Solution:
    ## Kadane's Algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        
        for n in nums:
            curSum = max(curSum, 0) # ensure sum is never negative
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum