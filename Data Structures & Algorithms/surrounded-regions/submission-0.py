class Solution:
    def solve(self, board: list[list[str]]) -> None:
        
        # Here we are using the DFS approach on the adjacency matrix

        # 1. SETUP: Get the height (ROWS) and width (COLS) of our board.
        ROWS, COLS = len(board), len(board[0])

        # 2. THE RESCUE WORKER (Helper Function)
        # This function finds 'O's that are safe and marks them with a 'T'.
        def capture(r, c):
            # If we step off the map, or if the current spot is NOT an "O", stop right here.
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return
            
            # We found a safe "O"! Change it to "T" (for Temporary/Safe) so we don't check it again.
            board[r][c] = "T"
            
            # Now, look Down, Up, Right, and Left to rescue any other "O"s connected to this one.
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 3. BORDER PATROL: An 'O' is only safe if it touches the edge (or is connected to one that does).
        # So, we walk around the very outer perimeter of the board looking for survivors.
        
        # Check the Left edge (column 0) and Right edge (last column) for every row.
        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        # Check the Top edge (row 0) and Bottom edge (last row) for every column.
        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        # 4. FINAL CLEANUP: Go through every single square on the board one last time.
        for r in range(ROWS):
            for c in range(COLS):
                
                # If a spot is STILL an "O", it means the rescue worker never reached it.
                # That means it was totally trapped in the middle! Change it to an "X".
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
                # If a spot is a "T", it was one of the safe ones we rescued earlier. 
                # Change it back to its original "O" shape.
                elif board[r][c] == "T":
                    board[r][c] = "O"