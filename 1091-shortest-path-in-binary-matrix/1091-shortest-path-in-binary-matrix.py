class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid)
        
        q = collections.deque([(0, 0, 1)])
        visited = set([(0, 0, 1)]) #r, c, length
        
        directions = [(-1, -1), (1, -1),(-1, 1),(1, 1),
                      (-1, 0), (0, -1), (0, 1), (1, 0)]
        while q:
            r, c, length = q.popleft()
            if (min(r, c) < 0 or max(r, c) >= ROWS or
                grid[r][c]):
                continue
            if r == ROWS - 1 and c == COLS - 1:
                return length
            for dr, dc in directions:
                if (r + dr, c + dc) not in visited:
                    q.append((r + dr, c + dc, length + 1))
                    visited.add((r + dr, c + dc))
        return -1    
                