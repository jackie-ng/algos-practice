class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        cnt, remaining = Counter(c.values()), len(c)
        for key in range(1, len(arr) + 1): # worst case if every element appears exact 1 time
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt[key]
            else:
                return remaining - k // key
        return remaining
    
        # hp = list(collections.Counter(arr).values())
        # heapq.heapify(hp)
        # while k > 0:
        #     k -= heapq.heappop(hp)
        # # returns the number of unique elements left in the array. 
        # # If k is negative after the last heap pop (which means the last popped count was larger than the remaining k), it adds 1 to the result.
        # return (len(hp) + 1) if k < 0 else len(hp)
