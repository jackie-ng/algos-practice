class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        if not grid:
            return 0
        
        def dfs(r, c):
            if (r not in range(ROWS)
               or c not in range(COLS)
               or (r, c) in visited
               or grid[r][c] == "0"):
                return
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands
       