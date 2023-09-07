class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # from collections import Counter
        # O(1) time
        if k == len(nums):
            return nums
        # 1. build hash map: character and how often it appears 
        #     O(N) time
        count = Counter(nums)
        # 2-3. build heal of top k frequent elements and convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)
        
        
        
        
        
  
        
        
        
        
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n, c in count.items():
#             freq[c].append(n)
            
#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
