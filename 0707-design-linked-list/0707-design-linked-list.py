class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, left, nextLeft = ListNode(val), self.left, self.left.next
        node.next, node.prev = nextLeft, left
        nextLeft.prev = node
        left.next = node

    def addAtTail(self, val: int) -> None:
        node, prevRight, right = ListNode(val), self.right.prev, self.right
        node.next, node.prev = right, prevRight
        right.prev = node
        prevRight.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        nextLeft = self.left.next
        while nextLeft and index > 0:
            nextLeft = nextLeft.next
            index -= 1
        
        if nextLeft and index == 0:
            node, prev = ListNode(val), nextLeft.prev
            node.next, node.prev = nextLeft, prev
            nextLeft.prev = node
            prev.next = node


    def deleteAtIndex(self, index: int) -> None:
        node = self.left.next
        while node and index > 0:
            node = node.next
            index -= 1
        
        if node and node != self.right and index == 0:
            node.prev.next = node.next
            node.next.prev = node.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)