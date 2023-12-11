class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        
class MyHashSet:
    # using linked list data structure for collision
    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)] # maximum number of keys based on the constraint

    def add(self, key: int) -> None:
        index = key % len(self.set) # create the hashmap key 
        cur = self.set[index] # head of the linked list
        
        while cur.next:
            if cur.next.key == key: # detect the duplicate
                return
            cur = cur.next
        # exits the loop, we'll find last node
        cur.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        index = key % len(self.set) # create the hashmap key 
        cur = self.set[index] # head of the linked list
        
        while cur.next:
            if cur.next.key == key: # detect the duplicate
                # remove
                cur.next = cur.next.next
                return
            cur = cur.next
    def contains(self, key: int) -> bool:
        index = key % len(self.set) # create the hashmap key 
        cur = self.set[index] # head of the linked list
        
        while cur.next:
            if cur.next.key == key: # detect the duplicate
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)