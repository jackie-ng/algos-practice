class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        #####Shorter solution####
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
        
#         self.stack.append((val))
#         # if the min stack is empty, or this number is smaller than
#         # the top of the min stack, put it on with a count of 1
#         if not self.min_stack or val < self.min_stack[-1][0]:
#             self.min_stack.append([val, 1])
#         # Else if this number is equal to what's currently at the top of the min stack,
#         # then increment the count at the top by 1
#         elif val == self.min_stack[-1][0]:
#             self.min_stack[-1][1] += 1


        
    def pop(self) -> None:
        #####Shorter solution####
        self.stack.pop()
        self.min_stack.pop()
        
        # if the top if min stack is the same as the top of the stack
        # then we need to decrement the count at the top by 1
#         if self.min_stack[-1][0] == self.stack[-1]:
#             self.min_stack[-1][1] -= 1
        
#         # if the count at the top of min stack is now 0,
#         # then remove that value as we're done with it
#         if self.min_stack[-1][1] == 0:
#             self.min_stack.pop()
            
#         # Pop the top of the main stack
#         self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()