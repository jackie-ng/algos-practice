class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # from collections import Counter
        # # O(1) time
        # if k == len(nums):
        #     return nums
        # # 1. build hash map: character and how often it appears 
        # #     O(N) time
        # count = Counter(nums)
        # # 2-3. build heap of top k frequent elements and convert it into an output array
        # # O(N log k) time
        # return heapq.nlargest(k, count.keys(), key=count.get)
        
        
        # i (count) 0 1 2 3 4 5 <--- go from the end of the freq array back. Freq = length of the input array
        # values     100  2 1    ---> 100 appear 1 time, 2 - 3 times, 1 - 4 times...
        
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        # print(freq)
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items(): # every single key, value pair in our dictionary
            freq[c].append(n) # value n occurs c times
            # print(freq)
            
        res = []
        for i in range(len(freq) - 1, 0, -1): # decensding order
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
