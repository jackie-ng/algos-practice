# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        groupPrev = dummy
        
        # 1 -> 2 -> 3
        # 1 -> 3 -> 2
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            
            # reverse group
            prev, curr = kth.next, groupPrev.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            #kth -- 1st node in the group
            tmp = groupPrev.next # 1st node in the group, kth is the last node in the group
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
            
            
    def getKth(self, curr, k):
        # pass curr, k: starting at curr, shift k times, return kth node
        # while curr is not in the end and k > 0 => update curr, decrement k
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    