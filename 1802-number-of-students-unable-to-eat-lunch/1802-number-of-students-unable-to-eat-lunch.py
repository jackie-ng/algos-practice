"""
1. Count the number of students preferring each sandwich type (count0, count1).
2. Iterate through each sandwich in the stack:
   │
   ├── If sandwich is 0 and count0 > 0:
   │     │→ Decrement count0.
   │
   ├── Else if sandwich is 1 and count1 > 0:
   │     │→ Decrement count1.
   │
   └── Else:
         │→ No more students want this sandwich → break.
3. Return count0 + count1 (students left without food).
"""
from collections import deque 
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # # 1. Brute force
        # queue = deque(students)
        # stack = sandwiches.copy()
        # unchanged = 0
        # # Continuously check if the front student wants the top sandwich.
        # while queue and unchanged < len(queue):
        #     # If yes, remove both the student and the sandwich
        #     if queue[0] == stack[0]:
        #         queue.popleft()
        #         stack.pop(0)
        #     # If no, move the student to the end of the queue.
        #     else:
        #         queue.append(queue.popleft())
        #         unchanged += 1
        # return len(queue)
        # 2. Optimal
        count = [0, 0]
        for s in students:
            count[s] += 1
        for s in sandwiches:
            if count[s] == 0:
                break
            count[s] -= 1
        return sum(count)