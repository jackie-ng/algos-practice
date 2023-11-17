class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         goal = len(nums) - 1
        
#         for i in range(len(nums) - 1, -1, -1):
#             if i + nums[i] >= goal:
#                 goal = i
#         return True if goal == 0 else False
    
        n = len(nums)
        memo = [None] * n

        def can_reach(position):
            # Base case: If the last index is reached, return True
            if position == n - 1:
                return True

            # If the result for the current position is already memoized, return it
            if memo[position] is not None:
                return memo[position]

            # Explore all possible jumps from the current position
            max_jump = min(position + nums[position], n - 1)
            for next_position in range(position + 1, max_jump + 1):
                if can_reach(next_position):
                    memo[position] = True
                    return True

            # If no jump leads to the last index, memoize and return False
            memo[position] = False
            return False

        return can_reach(0)