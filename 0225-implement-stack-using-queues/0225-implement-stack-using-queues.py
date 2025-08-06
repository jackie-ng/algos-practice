from collections import deque
class MyStack:
    # # 2 queues
    # def __init__(self):
    #     self.q1 = deque()
    #     self.q2 = deque()
    # # Push Operation:
    # # Move all elements from q1 to q2.
    # # Add the new element to q1.
    # # Move all elements back from q2 to q1.
    # def push(self, x: int) -> None:
    #     self.q2.append(x)
    #     while self.q1:
    #         self.q2.append(self.q1.popleft())
    #     self.q1, self.q2 = self.q2, self.q1

    # def pop(self) -> int:
    #     return self.q1.popleft()

    # def top(self) -> int:
    #     return self.q1[0]

    # def empty(self) -> bool:
    #     return not self.q1
    # 1 queue
    def __init__(self):
        self.q = deque()
    
    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()