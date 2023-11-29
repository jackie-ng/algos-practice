class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         res = []
#         subset = []
        
#         # decrease the target everytime we traverse
#         def backtrack(pos, target):
#             if target == 0:
#                 res.append(subset[:])
#                 return
#             if target <= 0:
#                 return
#             prev = -1
#             for i in range(pos, len(candidates)):
#                 # if current candidate is equal to the previous candidate =>  skip
#                 if candidates[i] == prev:
#                     continue
#                 subset.append(candidates[i])
#                 backtrack(i + 1, target - candidates[i])
#                 subset.pop()
#                 prev = candidates[i]
        
#         backtrack(0, target)
#         return res
        nums.sort()
        res = []
        subset = []
        
        def backtrack(pos, sum):
            if sum == target:
                res.append(subset[:])
                return
            if sum > target:
                return
            prev = -1
            for i in range(pos, len(nums)):
                if nums[i] == prev:
                    continue
                subset.append(nums[i])
                backtrack(i+1, sum+nums[i])
                subset.pop()
                prev = nums[i]
        backtrack(0, 0)
        return res
        