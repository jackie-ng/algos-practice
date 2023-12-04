class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         rows, cols = len(matrix), len(matrix[0])
#         if rows == 0:
#             return 0
        
#         indegree = [[0 for x in range(cols)] for y in range(rows)] 
#         directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
#         for x in range(rows):
#             for y in range(cols):
#                 for direction in directions:
#                     nx, ny = x + direction[0], y + direction[1]
#                     if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
#                         if matrix[nx][ny] < matrix[x][y]:
#                             indegree[x][y] += 1
                            
#         queue = []
#         for x in range(rows):
#             for y in range(cols):
#                 if indegree[x][y] == 0:
#                     queue.append((x, y))
    
#         path_len = 0
#         while queue:
#             sz = len(queue)
#             for i in range(sz):
#                 x, y = queue.pop(0)
#                 for direction in directions:
#                     nx, ny = x + direction[0], y + direction[1]
#                     if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
#                         if matrix[nx][ny] > matrix[x][y]:
#                             indegree[nx][ny] -= 1
#                             if indegree[nx][ny] == 0:
#                                 queue.append((nx, ny))
#             path_len += 1
#         return path_len 
    
         # dfs
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(pre, r, c):
            # preorder
            if r in {-1, rows} or c in {-1, cols} or pre >= matrix[r][c]: # out of bounds
                return 0
            
            if (r, c) in memo: 
                return memo[(r, c)]
            
            # traverse neighber
            memo[(r, c)] = 1 + max(dfs(matrix[r][c], r+i, c+j) for (i, j) in dirs)
            return memo[(r, c)]
        
        
        return max(dfs(-1, r, c) for r in range(rows) for c in range(cols))