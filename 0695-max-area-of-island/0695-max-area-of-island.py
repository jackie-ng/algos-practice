class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        area = 0
        def dfs(r, c):
            # if r, c are out of bound
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == 0 or
               (r, c) in visited):
                return 0
            # if the position is not out of bound, add to visited
            visited.add((r, c))
            # traverse and add total to the output
            return (1 + dfs(r + 1, c)
                    + dfs(r, c + 1)
                    + dfs(r - 1, c)
                    + dfs(r, c - 1))
        
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        return area
                