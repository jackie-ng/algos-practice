# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev, cur = None, head
        # while cur:
        #     cur.next, cur, prev = prev, cur.next, cur
        # return prev

        if not head:
            return None
        cur = head
        if head.next:
            cur = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return cur

# On Node 1
# Node for head.next is 2
# Setting node 2.next = 1 (head.next.next = head)
# 1->2->1
# Setting 1-> to null to remove. (head.next = None)
# 2->1