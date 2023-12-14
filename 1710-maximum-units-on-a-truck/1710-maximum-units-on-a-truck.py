class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        boxes = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                boxes += box * units
            else:
                boxes += truckSize * units
                return boxes
        return boxes
    
#         boxes, cur_units, cnt = 0, 1000, Counter()
#         for box, units in boxTypes:
#             cnt[units] += box
#         while cur_units > 0:
#             if cnt[cur_units] > 0:
#                 fit_in = min(truckSize, cnt[cur_units])    
#                 boxes += fit_in * cur_units
#                 truckSize -= fit_in
#                 if truckSize == 0:
#                     return boxes
#             cur_units -= 1
#         return boxes

#         freq, max_units = [0]*1001, 0
#         for box in boxTypes:
#             freq[box[1]] += box[0]
#         for units in range(1000,0,-1):
#             if truckSize < 0: break
#             max_units += min(truckSize, freq[units]) * units
#             truckSize -= freq[units]
#         return max_units