"""
1.merge sort

2. 
"""
"""
1. Ensure nums1 is the smaller array (swap if needed)
   │
2. Initialize binary search boundaries (left=0, right=len(nums1))
   │
3. While left <= right:
   │   a. Partition nums1 at mid = (left + right) // 2
   │   b. Partition nums2 at (total_len + 1) // 2 - mid
   │   c. Check if partitions are correct:
   │      ├── If max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
   │      │     │→ Correct partition found → Calculate median
   │      │
   │      ├── Else if max_left_nums1 > min_right_nums2:
   │      │     │→ Move partition left (right = mid - 1)
   │      │
   │      └── Else:
   │            │→ Move partition right (left = mid + 1)
   │
4. Handle edge cases (empty arrays, partitions at boundaries)

***Test case 1:
Step 1: nums1 is smaller, proceed
Step 2: left=0, right=2
Iteration 1:
  mid = 1 → Partition nums1 at index 1: left=[1], right=[3]
  Partition nums2 at (3+1)//2 - 1 = 1 → left=[2], right=[]
  Check:
    max_left = max(1, 2) = 2
    min_right = min(3, inf) = 3
    Since 2 <= 3 → Correct partition!
  Median = max_left = 2

***Test case 2:
Step 1: nums1 is smaller, proceed
Step 2: left=0, right=2
Iteration 1:
  mid = 1 → Partition nums1 at index 1: left=[1], right=[2]
  Partition nums2 at (4+1)//2 - 1 = 1 → left=[3], right=[4]
  Check:
    max_left = max(1, 3) = 3
    min_right = min(2, 4) = 2
    Since 3 > 2 → Incorrect! Move left (right = mid - 1)
Iteration 2:
  mid = 0 → Partition nums1 at index 0: left=[], right=[1,2]
  Partition nums2 at (4+1)//2 - 0 = 2 → left=[3,4], right=[]
  Check:
    max_left = max(-inf, 3) = 3
    min_right = min(1, inf) = 1
    Since 3 > 1 → Incorrect! Move right (left = mid + 1)
Iteration 3:
  mid = 1 → Same as Iteration 1 → Terminate
Final Partition:
  Correct partition is mid=1 for nums1 and mid=1 for nums2
  max_left = max(2, 3) = 3
  min_right = min(inf, 4) = 4
  Median = (3 + 4) / 2 = 3.5
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        total_len = m + n
        
        while left <= right:
            partition_nums1 = (left + right) // 2
            partition_nums2 = (total_len + 1) // 2 - partition_nums1
            
            max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = float('inf') if partition_nums1 == m else nums1[partition_nums1]
            
            max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = float('inf') if partition_nums2 == n else nums2[partition_nums2]
            
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if total_len % 2 == 0:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
                else:
                    return max(max_left_nums1, max_left_nums2)
            elif max_left_nums1 > min_right_nums2:
                right = partition_nums1 - 1
            else:
                left = partition_nums1 + 1
        return 0.0  # Should never reach here for valid inputs