class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = {}
        
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            first = minHeap[0]
            
            for i in range(first, first + groupSize):
                if i not in count: # if i value is not in the hashmap => val we're looking for is not available
                    return False
                count[i] -= 1 # if available, decrement count -1
                if count[i] == 0:
                    if i != minHeap[0]: # not able to complete next group as it's not the top of the heap
                        return False
                    heapq.heappop(minHeap)
        return True