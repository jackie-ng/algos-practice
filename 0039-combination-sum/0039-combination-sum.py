class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
        total = 0
        
        def backtracking(i, total):
            if total == target:
                res.append(subset.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            subset.append(candidates[i])
            backtracking(i, total + candidates[i])
            
            subset.pop()
            backtracking(i+1, total)
        
        backtracking(0, 0)
        return res
                