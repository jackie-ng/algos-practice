class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = [0] * 26  # Assuming uppercase English letters
        for task in tasks:
            task_count[ord(task) - ord('A')] += 1

        max_count = max(task_count)
        max_count_tasks = task_count.count(max_count)

        # Calculate the total units needed
        total_units = (max_count - 1) * (n + 1) + max_count_tasks

        return max(total_units, len(tasks))
    
#     ##SOLVING THIS USING HEAP##
    
#         # Count the frequency of each task
#         count = Counter(tasks)
        
#         # Create a max heap with negative frequencies
#         maxHeap = [-cnt for cnt in count.values()]
#         heapq.heapify(maxHeap)

#         # Initialize time and a deque to store pairs of [-cnt, idleTime]
#         time = 0
#         q = deque()

#         # Continue until both the maxHeap and the deque are empty
#         while maxHeap or q:
#             time += 1

#             # If maxHeap is empty, there are no tasks left to schedule
#             if not maxHeap:
#                 time = q[0][1]
#             else:
#                 # Schedule a task and update the maxHeap
#                 cnt = 1 + heapq.heappop(maxHeap)
#                 if cnt:
#                     # Add the task and its idle time to the deque
#                     q.append([cnt, time + n])

#             # If there are tasks in the deque ready to be scheduled, update the maxHeap
#             if q and q[0][1] == time:
#                 heapq.heappush(maxHeap, q.popleft()[0])

#         # The final value of 'time' represents the least number of units of time
#         return time