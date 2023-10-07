# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0) # for edge case
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0 # value of l1 if l1 is NOT null else, automatically set to 0
            l2Val = l2.val if l2 else 0
            
            # new digit

            columnSum = l1Val + l2Val + carry
            # calculate new carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            # update pointers
            curr.next = newNode
            # update l1 and l2 pointers if they're not NULL
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next