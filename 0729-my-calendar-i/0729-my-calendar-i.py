class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
class MyCalendar:

    def __init__(self):
        self.root = None

    def insert(self, start:int, end: int, node: Node) -> (Node, bool):
        # if the calendar is empty => insert the node and its values
        if not node:
            return Node(start, end), True
        # if the start OR end is between the interval start/end 
        # OR  the interval start/end cover the start AND end of the node
        if node.start <= start < node.end or node.start < end <= node.end or (start < node.start and end > node.end):
            return node, False
        
        if start < node.start:
            node.left, success = self.insert(start, end, node.left)
        else:
            node.right, success = self.insert(start, end, node.right)
        return node, success

        
    def book(self, start: int, end: int) -> bool:
        self.root, success = self.insert(start, end, self.root)
        return success


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)