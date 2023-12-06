class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        visited = {(0, 0)}
        pq = [(grid[0][0], 0, 0)]
        ans = 0
        while pq:
            depth, r, c = heapq.heappop(pq)
            ans = max(ans, depth)
            if r == c == N-1: 
                return ans
            for dr, dc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= dr < N and 0 <= dc < N and (dr, dc) not in visited:
                    heapq.heappush(pq, (grid[dr][dc], dr, dc))
                    visited.add((dr, dc))