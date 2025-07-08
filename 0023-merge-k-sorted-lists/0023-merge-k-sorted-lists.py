# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1, l2):
            dummy = ListNode()
            head = dummy  # Pointer to build the merged list
            while l1 and l2:
                if l1.val <= l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                head = head.next  # Move head forward
            
            # Attach the remaining part of l1 or l2
            if l1:
                head.next = l1
            else:
                head.next = l2
                
            return dummy.next  # Return the next node to skip dummy node
        
        # Merge each list one by one
        mergeList = None
        for l in lists:
            mergeList = merge2Lists(l, mergeList)
            
        return mergeList
