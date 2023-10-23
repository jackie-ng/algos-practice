class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                # if the position is empty -> skip
                if board[r][c] == ".":
                    continue
                cur = board[r][c]
                # if the value is already in the hash set => duplicate => invalid
                if (cur in cols[c] or cur in rows[r] or
                    cur in squares[(r//3, c//3)]):
                    return False
                # if the value is distinct, add to the hash sets
                cols[c].add(cur)
                rows[r].add(cur)
                squares[(r//3, c//3)].add(cur)
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