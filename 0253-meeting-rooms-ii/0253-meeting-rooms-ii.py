class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sum of rooms = sum of overlappping intervals
        # sort start, end of each meeting independently
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        # initialize res, count 
        res, count = 0, 0

        # initialize s (start), e (end) pointer
        s, e = 0, 0
        
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res

# start = [0, 5, 15]
# 	    s
# end =  [10, 20, 30]
# 	    e
# start[s] = 0
# end[e] = 10
# count = 0 + 1
# res=max(0,1)=1

# Move s += 1
# start[s] = 5
# end[e] = 10
# count = 1 + 1=2
# res = max(1,2) = 2

# Move s += 1
# start[s] = 15
# end[e] = 10
# count=2-1=1
# res=max(2,1)=2

# Move e += 1
# start[s] = 15
# end[e] = 20
# count=1+1=2
# res=max(2,2)=2

# Move s += 1 
# Out of bound
# return res = 2
