class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            # if c is not in the hashmap
            if c not in cur.children:
                cur.children[c] = TrieNode()
                
            # if c exists in the hashmap
            cur = cur.children[c]
        # mark is as end of the loop
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return False
            # move to the next node
            cur = cur.children[c]
        #if endOfWord is true => reach to the entire word => word is in the Trie
        return cur.endOfWord
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            # move to the next node
            cur = cur.children[c]
        # if we reach cur, return True
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)