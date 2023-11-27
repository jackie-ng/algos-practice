# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # # base case: recursion stops when we reach the end of the linkedlist 
        # if not list1 or list2 and list2.val < list1.val:
        #     list1, list2 = list2, list1
        # # recursion case: 
        # if list1:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        # return list1
    
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

