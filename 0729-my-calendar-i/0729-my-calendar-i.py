class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:
    def __init__(self):
        self.root = None

    def insert(self, start: int, end: int, node: Node) -> (Node, bool):
        if not node:
            # base case, insertion is successful
            return Node(start, end), True
        if node.start <= start < node.end or node.start < end <= node.end or (start < node.start and end > node.end):
            # if the interval to be inserted collides with existing interval, report error
            return node, False
        if start < node.start:
            node.left, success = self.insert(start, end, node.left)
        else:
            node.right, success = self.insert(start, end, node.right)
        return node, success

    def book(self, start: int, end: int) -> bool:
        self.root, success = self.insert(start, end, self.root)
        return success


# """boundary count based solution ~ 7000 ms"""


# from collections import Counter


# class MyCalendar:
#     def __init__(self):
#         self.delta = Counter()

#     def book(self, start, end) -> bool:
#         self.delta[start] += 1
#         self.delta[end] -= 1

#         active = 0
#         for boundary in sorted(self.delta):
#             active += self.delta[boundary]
#             if active > 1:
#                 # revert the updates
#                 self.delta[start] -= 1
#                 self.delta[end] += 1
#                 return False
#         return True