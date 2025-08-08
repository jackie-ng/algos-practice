"""
1. Calculate the Total Sum
2. Iterate with Left Sum: Iterate through array, maintaining a running left sum. 
For each index, compute the right_sum = total_sum - left_sum - nums[i]
3. Check Pivot: If left_sum = right_sum => current_index
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1        