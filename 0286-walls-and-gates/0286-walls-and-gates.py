import collections

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return

        ROWS, COLS = len(rooms), len(rooms[0])
        INF = 2147483647
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        q = deque()

        # 1) Enqueue all gates
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))

        # 2) Multi-source BFS
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # Only expand into INF rooms
                if 0 <= nr < ROWS and 0 <= nc < COLS and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))
