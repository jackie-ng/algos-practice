class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        if not grid:
            return 0
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                
                directions= [[1,0],[-1,0],[0,1],[0,-1]]
               
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and 
                        grid[r][c] == '1' and 
                        (r ,c) not in visited):
                        q.append((r , c ))
                        visited.add((r, c ))
                        
#             if (r not in range(ROWS) or
#                 c not in range(COLS) or
#                 (r, c) in visited):
#                 return
            
#             visited.add((r, c))
#             dfs(r + 1, c)
#             dfs(r, c + 1)
#             dfs(r - 1, c)
#             dfs(r, c - 1)
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
                    # dfs(r, c)
        return islands

    
