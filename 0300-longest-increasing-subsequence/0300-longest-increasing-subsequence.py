class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        
#         if not nums:
#             return 0
#         # Initializes an array tails to keep track of the tails of the increasing subsequences.

#         tails = [0] * len(nums)
#         length = 0

#         # The binary_search_insert function performs binary search to find the position where the current element can be inserted in the increasing subsequence.
#         def binary_search_insert(tails, target, length):
#             low, high = 0, length - 1

#             while low <= high:
#                 mid = (low + high) // 2
#                 if tails[mid] == target:
#                     return mid
#                 elif tails[mid] < target:
#                     low = mid + 1
#                 else:
#                     high = mid - 1

#             return low

#         # The final result is the length of the LIS.
#         # Time complexity of O(n log n), where n is the length of the input array nums. 
#         # The binary search ensures efficient insertion and updating of elements in the tails array.
#         # For each element in the input array nums, the algorithm finds its position in the tails array using binary search.
#         # If the position is equal to the current length, it means a new element is added, so increment the length.
#         # Otherwise, update the element at that position with the current element.
#         for num in nums:
#             pos = binary_search_insert(tails, num, length)

#             tails[pos] = num
#             if pos == length:
#                 length += 1

#         return length
    

#         # Dictionary to store memoized results
#         memo = {}

#         def lis_recursive(prev_index, current_index):
#             # Base case: if the end of the array is reached
#             if current_index == len(nums):
#                 return 0

#             # Check if the result is already memoized
#             if (prev_index, current_index) in memo:
#                 return memo[(prev_index, current_index)]

#             # Case 1: Include the current element if it is greater than the previous element
#             include_current = 0
#             if prev_index == -1 or nums[current_index] > nums[prev_index]:
#                 include_current = 1 + lis_recursive(current_index, current_index + 1)

#             # Case 2: Exclude the current element
#             exclude_current = lis_recursive(prev_index, current_index + 1)

#             # Update the memoization dictionary with the maximum of the two cases
#             memo[(prev_index, current_index)] = max(include_current, exclude_current)

#             return memo[(prev_index, current_index)]

#         # Start the recursion from the beginning of the array
#         return lis_recursive(-1, 0)

