#GREEDY ALGORITHM
"""
Greedy Approach: Select intervals in a way that leaves the maximum number of non-overlapping intervals.
Sorting: Sort intervals by their end times to prioritize intervals that finish earliest.
Overlap Detection: An interval overlaps with the last selected interval if its start time is less than the end time of the last selected interval.
1. Sort intervals based on end times.
2. Initialize:
   │→ last_end = -infinity (to compare with first interval)
   │→ count = 0 (number of intervals to remove)
3. For each interval in sorted list:
   │
   ├── If interval's start >= last_end:
   │     │→ No overlap, update last_end to current interval's end.
   │
   └── Else:
         │→ Overlap detected, increment count.
4. Return count.
Time Complexity: O(n log n) (due to sorting)
Space Complexity: O(1)
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])  # Sort by end times
        last_end = float('-inf')
        count = 0
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                count += 1
        return count
        # [[1,2], [1,3], [2,3],[3,4]]