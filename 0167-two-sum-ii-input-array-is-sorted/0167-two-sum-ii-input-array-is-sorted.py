"""
1. Initialize two pointers: left = 0, right = len(numbers) - 1.
2. While left < right:
   │
   ├── Calculate current sum: numbers[left] + numbers[right].
   │
   ├── If sum == target:
   │     │→ Return [left + 1, right + 1] (1-based indices).
   │
   ├── If sum < target:
   │     │→ Move left pointer right (left += 1).
   │
   └── If sum > target:
         │→ Move right pointer left (right -= 1).

"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total < target:
                left +=1
            else:
                right-=1
        return [-1,-1]
