class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
# Base case for empty list or empty 2d list
        if not events or not events[0]:
            return 0
        sorted_events = list(sorted(events,key=lambda x:x[0]))
        i = 0
        n = len(sorted_events)
        hp = []
        cur_day = 0
        count = 0
        while i < n or hp:
            # No day exists in heap, 
            # Pick current starting day
            if not hp:
                cur_day = sorted_events[i][0]
            
            # Iterate over events that have 
            # Same starting day as current day
            # And add their end days to min heap
            while i < n and cur_day == sorted_events[i][0]:
                heappush(hp,sorted_events[i][1])
                i += 1
            
            # Pop the earliest ending event
            heappop(hp)
            
            # Increase count
            count += 1
            
            # Increase current day (to mark one day of event attended)
            cur_day += 1
            
            # If current day has exceeded any 
            # event end time, we cant attend it, 
            # Pop it
            while hp and cur_day > hp[0]:
                heappop(hp)
            
        return count