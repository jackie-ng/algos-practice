class ListNode:
    def __init__(self, val, nxt, prev):
        self.val, self.next, self.prev = val, nxt, prev
class MyCircularQueue:
    
    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None) # left dummy node
        self.right = ListNode(0, None, self.left) # right dummy node
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        # assign ListNode with the value and left+right pointers
        cur = ListNode(value, self.right, self.right.prev)
   
        # updating the next attribute of the node that is currently the predecessor of self.right dummy node
        # it adjusts the next pointer of the node before the right dummy node to point to the newly created node cur. 
        # Effectively inserts cur into the linked list after the node referenced by self.right.prev.
        self.right.prev.next = cur
        # updates the prev attribute of self.right to point to the newly created node cur. 
        # After this line executes, self.right.prev becomes the new last node in the circular queue.
        self.right.prev = cur
        
        # update the space after enQueue    
        self.space -= 1
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        # Update the next attribute of the node that is currently the successor of self.left. 
        # it adjusts the next pointer of the node after the left dummy node to skip the current front node. 
        # By doing this, it effectively removes the front node from the linked list.
        self.left.next = self.left.next.next
        # updating the prev attribute of the node that is now the new front node in the circular queue. 
        # It sets the prev pointer of the new front node to point back to the left dummy node. 
        # This ensures that the circular structure is maintained, and the new front node correctly points to the left dummy node.
        self.left.next.prev = self.left
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        # isEmpty is true when there's only left and right dummy nodes exist
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()