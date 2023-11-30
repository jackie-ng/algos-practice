class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[0])
        
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]: # check the remaining intervals
            # if start of current interval >= end of previous interval
            # => not overlapping
            if start >= prevEnd: # not overlapping
                prevEnd = end # update the prevEnd to the newEnd
            # else, there is an overlap => increase res by 1
            # => update previous end to the minimum between the previous and the current interval
            else:
                res += 1
                prevEnd = min(end, prevEnd) # update prevEnd
            
        return res
                