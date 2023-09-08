class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
    
#             N = 9

#         # Use hash set to record the status
#         rows = [set() for _ in range(N)]
#         cols = [set() for _ in range(N)]
#         boxes = [set() for _ in range(N)]

#         for r in range(N):
#             for c in range(N):
#                 val = board[r][c]
#                 # Check if the position is filled with number
#                 if val == ".":
#                     continue

#                 # Check the row
#                 if val in rows[r]:
#                     return False
#                 rows[r].add(val)

#                 # Check the column
#                 if val in cols[c]:
#                     return False
#                 cols[c].add(val)

#                 # Check the box
#                 idx = (r // 3) * 3 + c // 3
#                 if val in boxes[idx]:
#                     return False
#                 boxes[idx].add(val)

#         return True