class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = -1
        while left <= right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h*w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
"""
1. Initialize two pointers: left = 0, right = len(height) - 1.
2. Initialize max_area = 0.
3. While left < right:
   │
   ├── Calculate current area: min(height[left], height[right]) * (right - left).
   │
   ├── Update max_area if current area is larger.
   │
   ├── Move the pointer pointing to the shorter line inward:
   │     ├── If height[left] < height[right]:
   │     │     │→ left += 1
   │     └── Else:
   │           │→ right -= 1
   │
   └── Return max_area.
"""