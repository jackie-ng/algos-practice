class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 12
        # position = [10,8,0,5,3]
        # speed = [2,4,1,1,3]
        # print(pair)
        # ---> [[10, 2], [8, 4], [0, 1], [5, 1], [3, 3]]
        pair = [[p, s] for p, s in zip(position, speed)] #list comprehension
        stack = []
        
        for p, s in sorted(pair)[::-1]: # Reverse Sorted order
             # time the car will reach the destination = (target - position) / speed
            stack.append((target - p) / s)
            # check if it's overlapped with the top of your stack
            # check if the stack has at least 2 elements
            # and if the top of the stack collied with the 2nd top of the stack => pop the top of the stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)