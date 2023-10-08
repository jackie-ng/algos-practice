class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None # 2 pointers: prev node and next node


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {}  # hash map: map key to node
        self.left, self.right = Node(0, 0), Node(0, 0) # dummy nodes. left=LRU, right=most recent
        self.left.next, self.right.prev = self.right, self.left # connect dummy nodes left <  -> right

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        # prev <--> cur <--> next => prev <--> next
    # insert node at right most position
    def insert(self, node):
        # retrieve the pointers
        prev, nxt = self.right.prev, self.right
        # reassign the pointers
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        # prev <--> right => prev <--> node <--> right

    def get(self, key: int) -> int:
        if key in self.cache:
            # everytime we map to a value, we want to update to the right most recent 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val # each key map to a node
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # Put the new node into the hash map
        self.cache[key] = Node(key, value)
        # Insert to the doubly linked list
        self.insert(self.cache[key])

        # Check the length of the cach exceed capacity ? remove the least recently use
        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
