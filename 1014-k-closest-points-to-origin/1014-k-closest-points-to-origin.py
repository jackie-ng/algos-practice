import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []
        heap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (-dist, x, y)) # farthest amoung kept sits at heap[0]
            if len(heap) > k:
                heapq.heappop(heap) # drop the current farthest
        # Extract k points (order doesn't matter)
        return [[x, y] for _, x, y in heap]
