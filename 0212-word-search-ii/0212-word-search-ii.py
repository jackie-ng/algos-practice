class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # mark this is the end of the word
        cur.isWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        # add each character to the trie
        for w in words:
            root.addWord(w)
            
        ROWS, COLS = len(board), len(board[0])
        
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            # if row, column is not inbound, or it's visited, or not in Trie node => return
            if (r < 0 or c < 0 or
               r == ROWS or c == COLS or
               (r, c) in visit or board[r][c] not in node.children):
                return
            
            # mark the current position as visited
            visit.add((r, c))
            node = node.children[board[r][c]] # update the node
            word += board[r][c] # update the word
            
            # check is it's the end of the word
            if node.isWord:
                res.add(word)
                
            dfs(r - 1, c, node, word) 
            dfs(r + 1, c, node, word)    
            dfs(r, c - 1, node, word)    
            dfs(r, c + 1, node, word)
            
            # remove from visited
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)      
        