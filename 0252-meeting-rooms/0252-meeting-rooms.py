class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # a person can attend all meetings if there are no overlapse
        # condition to overlap: when the end of this meeting > the starting of next meeting
        #-> as we can see, its very important to get the right order of the meeting because we would always compare the end of meeting X with the starting of meeting X +1 
        # -> we need to sort meeting based on starting times
        if len(intervals) == 0 or len(intervals) == 1:
            return True
        intervals = sorted(intervals, key = lambda x:x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True