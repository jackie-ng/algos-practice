# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
 2 4 3 
 5 6 4
 7 0 8


"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Create a dummy node to simplify handling the head of the result list
        cur = dummy         # Pointer to build the new linked list
        carry = 0           # Initialize carry for digits summing
        total = 0           # Initialize total (used inside the loop)

        while l1 or l2 or carry:  # Continue while either list has nodes left or there is a carry
            # Get value
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            total = num1 + num2 + carry
            val = total % 10
            # Create and append the new node with that digit
            cur.next = ListNode(val)
            # Update carry (any value over 9 will carry to next digit)
            carry = total // 10
            # Move the current pointer to the new node
            cur = cur.next
            # Move to the next node if it's not None
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None

        return dummy.next  # Return the head of the new linked list (skip dummy node)