class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # maxHeap using units
        pq = [[-boxTypes[i][1],boxTypes[i][0]] for i in range(len(boxTypes))]
        heapq.heapify(pq)
        ans = 0
        
        while truckSize != 0 and len(pq) != 0:
            units, boxes = heapq.heappop(pq)
            ans += min(boxes, truckSize) * (-units)
            truckSize -= min(boxes, truckSize)
        return ans
        
#         boxTypes.sort(key=lambda x: -x[1])
#         totalUnits = 0
        
#         for box, units in boxTypes:
#             if truckSize > box: # if we still have space, add more box
#                 truckSize -= box
#                 totalUnits += box * units
#             else: # if we run out of space, add the remaining truckSize * units to the totalUnits
#                 totalUnits += truckSize * units
#                 return totalUnits
        
#         return totalUnits
    
      