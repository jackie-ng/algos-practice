class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i:i[0]) # sort based on the start meeting time
        # loop through intervals array to check every single meeting
        for i in range(1, len(intervals)):
            i1 = intervals[i-1] # previous meeting
            i2 = intervals[i] # current meeting
            # if the end time of previous meeting > the start time of current meeting => False
            if i1[1] > i2[0]: 
                return False
        return True