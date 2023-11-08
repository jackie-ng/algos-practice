class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            cur = intervals[i]
            
            if cur[1] < newInterval[0]:
                res.append(cur)
            elif newInterval[1] < cur[0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [ min(newInterval[0], cur[0]), max(newInterval[1], cur[1]) ]
        res.append(newInterval)
        return res