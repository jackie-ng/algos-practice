class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                # Update minimum index
                if nums[j] < nums[min_index]:
                    min_index = j

            # Swap current index with minimum element in rest of list
            nums[min_index], nums[i] = nums[i], nums[min_index]