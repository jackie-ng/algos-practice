import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap via negatives
        self.hi = []  # min-heap

    def addNum(self, num: int) -> None:
        # Step 1: push to lo (max-heap)
        heapq.heappush(self.lo, -num)

        # Step 2: balance order: top(lo) <= top(hi)
        if self.hi and (-self.lo[0] > self.hi[0]):
            x = -heapq.heappop(self.lo)
            heapq.heappush(self.hi, x)

        # Step 3: balance sizes: len(lo) >= len(hi) and diff <= 1
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
        elif len(self.lo) - len(self.hi) > 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2.0
