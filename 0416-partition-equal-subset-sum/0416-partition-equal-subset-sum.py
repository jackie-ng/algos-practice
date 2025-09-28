"""
1. i think it's essential to sort the array? 

2. 
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # # Memoization
        # # find sum of array elements
        # total_sum = sum(nums)
        # # if total_sum is odd, it cannot be partitioned into equal sum subsets
        # if total_sum % 2 != 0:
        #     return False
        # # target sum
        # subset_sum = total_sum // 2
        # n = len(nums)

        # @lru_cache(maxsize=None)
        # def dfs(nums: Tuple[int], n: int, subset_sum: int) -> bool:
        #     # Base cases
        #     if subset_sum == 0:
        #         return True
        #     # no items left or remaining sum negative -> fail
        #     if n == 0 or subset_sum < 0:
        #         return False
        #     result = (dfs(nums, n - 1, subset_sum) # Option 1: skip nums[i]
        #             or dfs(nums, n - 1, subset_sum - nums[n - 1]) # Option 2: take nums[i]
        #             )
        #     return result



        # return dfs(tuple(nums), n - 1, subset_sum)
        #------------------------------
        ## DP 2-D
        # total = sum(nums)
        # if total % 2 == 1:
        #     return False
        # target = total // 2
        # n = len(nums)

        # dp = [[False] * (target + 1) for _ in range(n + 1)]
        # dp[0][0] = True

        # for i in range(1, n + 1):
        #     v = nums[i - 1]
        #     for s in range(target + 1):
        #         dp[i][s] = dp[i - 1][s] or (s >= v and dp[i - 1][s - v])
        # return dp[n][target]
        ## DP 1-D
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for v in nums:
            # iterate backwards to avoid reusing the same number
            for s in range(target, v - 1, -1):
                if dp[s - v]:
                    dp[s] = True
            # optional early exit
            if dp[target]:
                return True

        return dp[target]