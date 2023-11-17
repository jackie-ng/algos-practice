class Solution:
    def jump(self, nums: List[int]) -> int:
                
        n = len(nums)
        jumps = 0
        current_end = 0  # The maximum index that can be reached with the current number of jumps
        farthest = 0     # The maximum index that can be reached with the next jump

        for i in range(n - 1):
            print(i, nums[i], farthest)
            farthest = max(farthest, i + nums[i])

            # If we have reached the current maximum reachable index, make a jump
            if i == current_end:
                current_end = farthest
                jumps += 1

        return jumps