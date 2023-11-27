# class ListNode:
#     def __init__(self, x):
# Definition for singly-linked list.
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: 
                break
        else: 
            return None  # if not (fast and fast.next): return None
        
        while head != slow:
            head, slow = head.next, slow.next
        return head