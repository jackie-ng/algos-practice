# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or list2 and list2.val < list1.val:
            list2, list1 = list1, list2
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
#         dummy = ListNode()
#         tail = dummy

#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 list2 = list2.next
#             tail = tail.next
        
#         if list1:
#             tail.next = list1
#         elif list2:
#             tail.next = list2 
#         return dummy.next
    
        # if list1 is None:
        #     return list2
        # elif list2 is None:
        #     return list1
        # elif list1.val < list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2
