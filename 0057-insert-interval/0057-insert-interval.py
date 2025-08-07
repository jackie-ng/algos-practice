"""
Sorted Intervals: The given intervals are already sorted by start time, which simplifies the insertion process.
Three Phases:
- Before: Intervals that end before the new interval starts.
- Merge: Intervals that overlap with the new interval, which need to be merged.
- After: Intervals that start after the new interval ends.
Merging: The merged interval's start is the minimum of the overlapping intervals' starts, and its end is the maximum of their ends.
1. Initialize an empty result list.
2. Iterate through each interval in the original list:
   │
   ├── If current interval ends before newInterval starts:
   │     │→ Add current interval to result.
   │
   ├── Else if current interval starts after newInterval ends:
   │     │→ Add newInterval to result.
   │     │→ Update newInterval to current interval (to avoid re-adding).
   │
   └── Else (overlap):
         │→ Merge current interval with newInterval:
         │     newInterval = [min(start1, start2), max(end1, end2)].
3. Add any remaining newInterval to result.
4. Return result.
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # # Time Complexity: O(n log n) (due to sorting)
        # # Space Complexity: O(n) (for the new list)
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x: x[0])
        # merged = []
        # for interval in intervals:
        #     if not merged or merged[-1][1] < interval[0]:
        #         merged.append(interval)
        #     else:
        #         merged[-1][1] = max(merged[-1][1], interval[1])
        # return merged
        result = []
        i = 0
        n = len(intervals)
        # Add intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Add intervals after newInterval
        while i < n:
            result.append(intervals[i])
            i += 1
        return result