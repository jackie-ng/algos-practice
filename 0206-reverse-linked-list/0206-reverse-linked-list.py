# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # 1. Iterative
        # curr_node, prev_node = head, None
        # while curr_node:
        #     next_node = curr_node.next
        #     curr_node.next = prev_node
        #     #update prev_node and curr_node
        #     prev_node = curr_node
        #     curr_node = next_node
        # # prev_node will be pointing at the head of the reversed linked list
        # return prev_node
        # 2. Recursive
        # Base case
        if (not head) or (not head.next):
            return head
        # Recursive case
        cur = head
        # if we haven't reached the end of the list, run recursion
        # on node 1, head = 1, head.next = 2, head.next.next = 3
        # set 2.next = 1 => we have 1->2->1->3
        # set head.next = None to destroy the pointer => 2->1->3
        if head.next:
            cur = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return cur
