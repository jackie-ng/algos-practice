# from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # O(1) time
        # if k == len(nums):
        #     return nums
        # # 1. build hash map: character and how often it appears 
        # #     O(N) time
        # count = Counter(nums)
        # # 2-3. build heap of top k frequent elements and convert it into an output array
        # # O(N log k) time
        # return heapq.nlargest(k, count.keys(), key=count.get)
        ########## Bucket Sort ############
        # i (count) 0 1 2 3 4 5 <--- go from the end of the freq array back. Freq = length of the input array
        # values     100  2 1    ---> 100 appear 1 time, 2 - 3 times, 1 - 4 times...
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res