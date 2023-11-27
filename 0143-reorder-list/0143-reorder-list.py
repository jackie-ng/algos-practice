# Find a middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Example: for the list 1->2->3->4->5->6, the middle element is 4.

# Once a middle node has been found, reverse the second part of the list.
# Example: convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4.

# Now merge the two sorted lists.
# Example: merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse second half
        secondHalf = slow.next
        slow.next = None
        prev = None
        while secondHalf:
            # For each current node, save its neighbours
            temp = secondHalf.next
            # change the node's next pointer to point to the previous node:
            secondHalf.next = prev
            # update pointers
            prev = secondHalf
            secondHalf = temp
        
        # Merge 2 lists
        firstHalf = head
        secondHalf = prev
        while secondHalf:
            temp1, temp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            # update pointers
            firstHalf, secondHalf = temp1, temp2
        
        
            
        