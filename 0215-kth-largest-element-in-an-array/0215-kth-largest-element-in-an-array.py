class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]        

# ### Quick Select ###
#         # target index -> reassign k
#         k = len(nums) - k
        
#         def quickSelect(l, r):
#             pivot, p = nums[r], l # p: left most value, pivot: right most value
#             for i in range(l, r):
#                 if nums[i] <= pivot:
#                     nums[p], nums[i] = nums[i], nums[p]
#                     p += 1
#             # swap pivot value with the index
#             nums[p], nums[r] = pivot, nums[p] # pivot = nums[r]
            
#             if p > k: # Run quick select on the left portion as we need to find a smaller index
#                 return quickSelect(l, p - 1)
#             elif p < k:
#                 return quickSelect(p + 1, r)
#             else:
#                 return nums[p]
        
#         return quickSelect(0, len(nums) - 1)
    