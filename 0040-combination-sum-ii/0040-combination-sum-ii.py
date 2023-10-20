class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        subset = []
        # decrease the target everytime we traverse
        def backtrack(pos, target):
            if target == 0:
                res.append(subset.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                # if current candidate is equal to the previous candidate =>  skip
                if candidates[i] == prev:
                    continue
                subset.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                subset.pop()
                prev = candidates[i]

        backtrack(0, target)
        return res
