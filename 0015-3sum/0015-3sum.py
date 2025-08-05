"""
1. Sort the array.
2. Iterate through each element (nums[i]):
   │
   ├── Skip duplicates: if nums[i] == nums[i-1], continue.
   │
   ├── Initialize two pointers: left = i+1, right = len(nums)-1.
   │
   ├── While left < right:
   │     │→ Calculate sum = nums[i] + nums[left] + nums[right].
   │     │
   │     ├── If sum == 0:
   │     │     │→ Add triplet to result.
   │     │     │→ Skip duplicates for left and right.
   │     │     │→ Move left++ and right--.
   │     │
   │     ├── If sum < 0:
   │     │     │→ Move left++ (need a larger sum).
   │     │
   │     └── If sum > 0:
   │           │→ Move right-- (need a smaller sum).
   │
   └── Return the result.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0: 
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1 
                    right -= 1
        return res