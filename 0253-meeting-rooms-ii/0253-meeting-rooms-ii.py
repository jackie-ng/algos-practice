class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals ])
        end = sorted([i[1] for i in intervals])
        
        res, count = 0, 0
        s, e = 0, 0 # pointer
        
        while s < len(intervals): # if the start pointer has NOT reach the end of the array
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
                
            res = max(res, count)
        return res
        