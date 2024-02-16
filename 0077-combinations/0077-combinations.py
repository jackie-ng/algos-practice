class Solution(object):
    def combine(self, n, k):
        res = []
        def backtrack(i, subset):
            if len(subset) == k:
                res.append(subset[:])
                return
            for num in range(i, n+1):
                subset.append(num)
                backtrack(num+1, subset)
                subset.pop()
        backtrack(1,[])
        return res