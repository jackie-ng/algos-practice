class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        print(numSet)
        longest = 0
        
        for n in nums:
            #check if it's the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
                
# # sorting
# class Solution:
#     def longestConsecutive(self, nums):
#         if not nums:
#             return 0

#         nums.sort()

#         longest_streak = 1
#         current_streak = 1

#         for i in range(1, len(nums)):
#             if nums[i] != nums[i-1]:
#                 if nums[i] == nums[i-1]+1:
#                     current_streak += 1
#                 else:
#                     longest_streak = max(longest_streak, current_streak)
#                     current_streak = 1

#         return max(longest_streak, current_streak)

