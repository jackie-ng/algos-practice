class MedianFinder:

    def __init__(self):
        # Initialize two heaps: a max heap (small) and a min heap (large)
        self.small = []  # Max heap to store the smaller half of elements
        self.large = []  # Min heap to store the larger half of elements

    def addNum(self, num: int) -> None:
        # Maintain the balance between the two heaps

        # If the number is greater than the smallest element in the large heap
        if self.large and num > self.large[0]:
            # Add the number to the large heap
            heapq.heappush(self.large, num)
        else:
            # Add the negation of the number to the small heap (max heap)
            heapq.heappush(self.small, -1 * num)

        # Rebalance the heaps if necessary
        # Ensure the size difference between the two heaps is at most 1
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # Find and return the median of the current elements

        if len(self.small) > len(self.large):
            # If small heap has more elements, return the top element of the small heap
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            # If large heap has more elements, return the top element of the large heap
            return self.large[0]
        else:
            # If both heaps have equal size, return the average of the top elements
            return (-1 * self.small[0] + self.large[0]) / 2
