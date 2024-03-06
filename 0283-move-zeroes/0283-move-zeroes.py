class Solution(object):
    def moveZeroes(self, nums):
        i = count = 0
        while count < len(nums):
            if nums[i] == 0: 
                nums.append(nums.pop(i))
            else: i += 1
            count += 1