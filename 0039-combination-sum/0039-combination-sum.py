class Solution(object):
    def combinationSum(self, nums, target):
        res = []
        subset = []
        sum = 0
        def backtrack(i, sum):
            if sum == target:
                res.append(subset[:])
                return
            # if the pointer is out-of-bound or sum larger that target
            if i >= len(nums) or sum > target:
                return
            # backtrack, include the current number
            subset.append(nums[i])
            backtrack(i, sum+nums[i])
            
            # backtrack, not include the current number
            subset.pop()
            backtrack(i+1, sum)
        backtrack(0,0)
        return res