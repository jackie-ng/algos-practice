class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]  # 4-directional
        q = deque()
        fresh = 0

        # Collect all rotten as multi-source BFS starts; count fresh
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0  # nothing to rot

        minutes = 0
        # BFS by levels; each level = 1 minute of spread
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2   # rot it
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1    
            