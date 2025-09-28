"""
- Smashing two stones x and y (with x ≤ y) replaces them with y-x (or removes both if equal). This process is equivalent to dividing the stones into two groups and taking the absolute difference of the sums of the two groups.
- Reason: each smash effectively moves one stone’s weight to the other with sign change; ultimately the remaining weight equals |sum(groupA) − sum(groupB)|. So we want to partition stones into two subsets whose sums are as close as possible.
- Let total = sum(stones). If one subset has sum s, the other has total - s. The final leftover weight is | (total - s) - s | = |total - 2s|. Minimizing that is equivalent to finding s as close as possible to total/2.
=> So the problem reduces to: find the maximum subset sum s ≤ total//2 and answer total - 2*s

*** Proof for the recurrence relation
- Let total = sum(stones). If some subset has sum s, leftover weight will be |total - 2*s|. We want minimize that, so choose s as large as possible but ≤ total/2.
*** Define boolean DP:
- dp[i][t] = can we reach sum t using first i stones (i from 0..n)
*** Consider stone stones[i-1] = v. Two choices:
- Do not take it → dp[i-1][t].
- Take it (if t ≥ v) → dp[i-1][t - v].
*** Thus:
dp[i][t] = dp[i-1][t] OR (t ≥ v and dp[i-1][t - v])
*** Base:
dp[0][0] = True
dp[0][t>0] = False

- We want the largest t ≤ total//2 with dp[n][t] = True, then answer total - 2*t.
- We can compress dp to 1-D dp[t] and iterate stones, updating t from total//2 down to v to ensure each stone used at most once.
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # # Memoization: split 2 sides of the stone and make them as equal as possible to minimize the result
        # stoneSum = sum(stones)
        # halfStoneSum = ceil(stoneSum / 2)

        # def dfs(i, total): 
        #     # If total so far >= halfStoneSum or if i reach the end of the stones list
        #     if total >= halfStoneSum or i == len(stones):
        #         otherPile = stoneSum - total
        #         return abs(total - otherPile) # smash them. Abs to make sure it's not negative
        #     if (i, total) in memo:
        #         return memo[(i, total)]

        #     memo[(i, total)] = min(dfs(i + 1, total), # not include cur val
        #                          dfs(i + 1, total + stones[i])) # include cur val at i
        #     return memo[(i, total)]

        # memo = {}
        # return dfs(0, 0)
        total = sum(stones)
        target = total // 2
        n = len(stones)

        @cache
        def dfs(i, s):
            # i: current index (0..n), s: current sum so far (<= target)
            if i == n:
                return s
            # Option 1: skip stone i
            best = dfs(i + 1, s)
            # Option 2: take stone i, if it doesn't exceed target
            if s + stones[i] <= target:
                best = max(best, dfs(i + 1, s + stones[i]))
            return best

        best_s = dfs(0, 0)
        return total - 2 * best_s
        
        # # Tabulation
    
        # total = sum(stones)
        # target = total // 2
        # dp = [False] * (target + 1)
        # dp[0] = True

        # for v in stones:
        #     # update backwards to avoid reuse
        #     for t in range(target, v - 1, -1):
        #         if dp[t - v]:
        #             dp[t] = True

        # # find best achievable t <= target
        # for t in range(target, -1, -1):
        #     if dp[t]:
        #         return total - 2 * t
        # return 0
