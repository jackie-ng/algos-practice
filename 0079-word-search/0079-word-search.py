class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            # check if the range it's inbound and not visited
            if (r < 0 or r >= ROWS or
               c < 0 or c >= COLS or
               word[i] != board[r][c] or (r, c) in visited):
                return False
            # if it's inbound, add to visited set
            visited.add((r, c))
            res = (dfs(r+1, c, i+1) or
                  dfs(r, c+1, i+1) or
                  dfs(r-1, c, i+1) or
                  dfs(r, c-1, i+1))
            # clear up for the next traversal
            visited.remove((r, c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False