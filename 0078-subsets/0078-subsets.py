class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def backtracking(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            backtracking(i + 1)
            # decision not to include nums[i]
            subset.pop()
            backtracking(i + 1)
            
        backtracking(0)
        return res