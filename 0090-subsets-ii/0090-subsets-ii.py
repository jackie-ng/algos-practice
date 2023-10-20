class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        nums.sort()
        
        def backtracking(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # All subsets that include nums[i]
            subset.append(nums[i])
            backtracking(i+1)
            
            # All subsets that don't include nums[i]
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtracking(i+1)
            
        backtracking(0)
        return res