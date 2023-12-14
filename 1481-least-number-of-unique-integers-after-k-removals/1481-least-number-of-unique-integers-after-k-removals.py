class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        c = Counter(arr)
        cnt, remaining = Counter(c.values()), len(c)
        for key in range(1, len(arr) + 1): 
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
        # return len(hp) + (k < 0)  