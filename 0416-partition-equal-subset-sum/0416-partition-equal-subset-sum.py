class Solution:
    def canPartition(self, nums: List[int]) -> bool:
#         if sum(nums) % 2:
#             return False
#         dp = set() # for unique values
#         dp.add(0)
#         target = sum(nums) // 2
        
#         for i in range(len(nums) -1, -1, -1):
#             nextDP = set()
#             for t in dp:
#                 nextDP.add(t + nums[i])
#                 nextDP.add(t) # save the previous values
#             dp = nextDP # reassign dp to the next DP set
#         return True if target in dp else False
    

            if not nums:
                return True
            n = len(nums)

            # If the total sum is odd, it cannot be divided into two equal subsets.
            if sum(nums) % 2 != 0:
                return False
            target = sum(nums)//2
            memo = {}

            def dfs(total, i):
                # Check if the state (index, current_sum) has already been visited.

                if (total, i) in memo:
                    return memo[(total, i)]
                if i == len(nums):
                    return False
                if total == 0:
                    return True
                # Recursive case: Try including and excluding the current element.

                memo[(total, i)] = dfs(total-nums[i], i+1) or dfs(total, i+1)
                return memo[(total, i)]

            return dfs(target, 0) 