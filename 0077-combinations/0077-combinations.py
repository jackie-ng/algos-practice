class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:       
        res  = []
        def backtrack(start, subset):
            if len(subset) == k:
                res.append(subset[:])
                return
            for num in range(start, n+1):
                subset.append(num)
                backtrack(num+1, subset)
                subset.pop()
        backtrack(1, [])
        return res