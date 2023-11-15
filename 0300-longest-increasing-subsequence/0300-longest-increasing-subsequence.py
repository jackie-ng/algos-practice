class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tails = [0] * len(nums)
        length = 0

        def binary_search_insert(tails, target, length):
            low, high = 0, length - 1

            while low <= high:
                mid = (low + high) // 2
                if tails[mid] == target:
                    return mid
                elif tails[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return low

        for num in nums:
            pos = binary_search_insert(tails, num, length)

            tails[pos] = num
            if pos == length:
                length += 1

        return length
    
# Initializes an array tails to keep track of the tails of the increasing subsequences.
# The binary_search_insert function performs binary search to find the position where the current element can be inserted in the increasing subsequence.
# For each element in the input array nums, the algorithm finds its position in the tails array using binary search.
# If the position is equal to the current length, it means a new element is added, so increment the length.
# Otherwise, update the element at that position with the current element.
# The final result is the length of the LIS.
# Time complexity of O(n log n), where n is the length of the input array nums. The binary search ensures efficient insertion and updating of elements in the tails array.





