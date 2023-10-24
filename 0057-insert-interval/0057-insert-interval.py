class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            cur = intervals[i]
            
            if newInterval[1] < cur[0] : # nerInterval end value < cur start val
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > cur[1]: # nerInterval end value > cur start val
                res.append(cur)
            else:
                newInterval = [min(newInterval[0], cur[0]), max(newInterval[1], cur[1])]
                
                
        res.append(newInterval)
        return res