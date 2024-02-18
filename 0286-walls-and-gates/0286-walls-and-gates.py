class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()
        dist = 0
        
        
        # find a gate
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0: 
                    q.append([r, c])
                    visit.add((r, c))
        def addRoom(r, c):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
               (r, c) in visit or rooms[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])
        
        # q now contains the position of the gate
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                rooms[r][c] = dist # change the gate to current dist
                addRoom(r + 1, c) 
                addRoom(r - 1, c) 
                addRoom(r, c + 1) 
                addRoom(r, c - 1)
            dist += 1
        
        