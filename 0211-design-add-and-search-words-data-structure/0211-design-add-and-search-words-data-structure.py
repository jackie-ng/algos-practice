class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                # c: current charater in word
                c = word[i]
                # If c is ".", it means it can match any character. 
                # So, the code recursively explores all possible children nodes for each character in the Trie.
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child): # reach the end of the word
                            return True
                    return False
                # checks if the character is in the current Trie node's children. 
                # If not, it means the word doesn't exist in the Trie, and the function returns False.
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)