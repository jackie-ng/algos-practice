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