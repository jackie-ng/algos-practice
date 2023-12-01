class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []

        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                size = r - l + 1
                heapq.heappush(minHeap, (size, r))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [ res[q] for q in queries ]
#         # size of interval = r - l + 1 (inclusive)
#         intervals.sort()
        
#         minHeap = []
#         # res: mapping each queries with the smallest size
#         # i for each interval position
#         res, i = {}, 0
        
#         for q in sorted(queries):
#             # While there are more intervals 
#             # left endpoint of the current interval <= current query point, 
#             # add the size of the interval and its right endpoint to the min heap.
#             while i < len(intervals) and intervals[i][0] <= q:
#                 l, r = intervals[i]
                
#                 heapq.heappush(minHeap, (r - l + 1, r))
#                 i += 1
#             # remove the invalid interval from the minHeap
#             while minHeap and minHeap[0][1] < q:
#                 heapq.heappop(minHeap)
            
#             res[q] = minHeap[0][0] if minHeap else -1
#         return [ res[q] for q in queries ]
    