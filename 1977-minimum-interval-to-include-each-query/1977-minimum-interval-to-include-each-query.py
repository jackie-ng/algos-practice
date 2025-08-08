"""
1. Sort Intervals by Left End: This allows us to efficiently find intervals that start before or at the query value.
2. Sort Queries: Process queries in sorted order to leverage previously computed information.
3. Use a Min-Heap: To keep track of intervals that could contain the current query value, prioritized by their size.
4. Process Queries:
- For each query, add all intervals that start before or at the query value to the heap.
- Remove intervals from the heap that end before the query value.
- The smallest valid interval (if any) is at the top of the heap.

Time Complexity: O(n log n + m log m + m log n) (sorting intervals, sorting queries, and heap operations).
Space Complexity: O(n + m) for storing intervals, queries, and the heap.

"""
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted((val, idx) for idx, val in enumerate(queries))
        res = [-1] * len(queries)
        heap = []
        i = 0
        n = len(intervals)
        
        for val, idx in sorted_queries:
            while i < n and intervals[i][0] <= val:
                left, right = intervals[i]
                size = right - left + 1
                heapq.heappush(heap, (size, left, right))
                i += 1
            
            while heap and heap[0][2] < val:
                heapq.heappop(heap)
            
            if heap:
                res[idx] = heap[0][0]
        
        return res