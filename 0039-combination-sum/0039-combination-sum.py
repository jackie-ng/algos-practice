class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
   
        res = []
        subset = []
        sum = 0
        
        def backtrack(i, sum):
            if sum == target:
                res.append(subset[:])
                return
            if i >= len(candidates) or sum > target:
                return
            
            subset.append(candidates[i])
            backtrack(i, sum+candidates[i])
            subset.pop()
            backtrack(i+1, sum)
            
        backtrack(0, 0)
        return res