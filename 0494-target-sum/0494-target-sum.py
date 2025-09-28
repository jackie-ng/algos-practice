"""
- Let P = sum of numbers assigned +, and N = sum of numbers assigned -.
- The required condition is P - N = target.
- Also P + N = total where total = sum(nums).
- Solve the two equations: P = (total + target) / 2.
- So the problem becomes: count the number of subsets of nums whose sum equals P (call this subset-sum count).
- If (total + target) is odd, or P is negative, no solution → return 0.
- Counting subset-sums is a standard DP problem (0/1 knapsack counting variants).

Special care: zeros — they multiply counts (each zero can go to P or not and doesn’t change sum). The DP formulation handles that naturally.

Recurrence
dp[i][s] = dp[i-1][s] + (s >= nums[i-1] ? dp[i-1][s - nums[i-1]] : 0)
Base: dp[0][0] = 1 (one way to make sum 0 with zero items), other dp[0][s>0] = 0.

compress to 1-D
dp[s] += dp[s - num]   (iterate s from P down to num)
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # #  Memoization
        # n = len(nums)
        # @cache
        # def dfs(i, cur):
        #     # i: current index, cur: current sum
        #     if i == n:
        #         return 1 if cur == target else 0
        #     # try adding +nums[i] and -nums[i]
        #     return dfs(i+1, cur + nums[i]) + dfs(i+1, cur - nums[i])
        # return dfs(0, 0)
        #---------------------------
        ## Tabulation
        total = sum(nums)
        # impossible if target bigger than total or parity mismatch
        if abs(target) > total or (total + target) % 2 == 1:
            return 0
        P = (total + target) // 2

        dp = [0] * (P + 1)
        dp[0] = 1  # one way to make sum 0 (choose nothing)

        for num in nums:
            # iterate backward so each num is used at most once
            for s in range(P, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[P]