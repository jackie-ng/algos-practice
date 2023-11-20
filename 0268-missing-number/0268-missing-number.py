class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        # Iterate through each index and element in nums
        for i, num in enumerate(nums):
            # XOR will cancel out everything except for the result
            missing ^= i ^ num
        return missing