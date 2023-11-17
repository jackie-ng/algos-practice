class Solution:
    def jump(self, nums: List[int]) -> int:
#         res = 0
#         l = r = 0
        
#         while r < len(nums) - 1: # while r pointer has not reach the end of nums
#             farthest = 0 # initialize farthest 
#             for i in range(l, r + 1): # for the range of the window
#                 farthest = max(farthest, i + nums[i]) # calculate the farthest jump can go
#             l = r + 1 # update left pointer to the next adjacent of right pointer 
#             r = farthest # update right pointer
#             res += 1 # increment result after each iteration
#         return res
                
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