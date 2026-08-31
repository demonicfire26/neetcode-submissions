from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        # Here we are using BFS on a adjacency matrix
        # 1. SETUP: Get the size of our island map.
        ROWS = len(heights)
        COLS = len(heights[0])
        
        # A simple cheat code for moving Up, Down, Right, Left.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Create two blank maps of the island to track our results.
        # 'False' means "Water cannot reach the ocean from here (or we haven't checked yet)".
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        # 2. THE WORKER: This function starts at the beach and walks backwards (uphill).
        def bfs(source, ocean):
            # 'source' is the list of all beaches touching this specific ocean.
            # We put them all in a waiting line.
            q = deque(source)
            
            # As long as there are spots in the line, keep working.
            while q:
                r, c = q.popleft()
                
                # Mark this spot as True! Water from here CAN reach this ocean.
                ocean[r][c] = True
                
                # Look at the 4 neighboring spots around where we are standing.
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # We only move to a neighbor IF:
                    # 1. It is actually on the map (not out of bounds).
                    # 2. We haven't already marked it as True.
                    # 3. THE TRICK: The neighbor is taller than (or equal to) us. 
                    # Because we are starting at the ocean and walking backwards, we must go UPHILL!
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        # It's a valid uphill step, so add it to the line to check its neighbors later.
                        q.append((nr, nc))

        # 3. PREPARATION: Gather all the starting spots (the beaches).
        pacific = []
        atlantic = []
        
        # The Pacific Ocean touches the Top row. The Atlantic touches the Bottom row.
        for c in range(COLS):
            pacific.append((0, c))               # Top edge
            atlantic.append((ROWS - 1, c))       # Bottom edge

        # The Pacific Ocean touches the Left column. The Atlantic touches the Right column.
        for r in range(ROWS):
            pacific.append((r, 0))               # Left edge
            atlantic.append((r, COLS - 1))       # Right edge

        # 4. SEND OUT THE WORKERS
        # Tell the worker to map out everywhere the Pacific water can reach.
        bfs(pacific, pac)
        
        # Tell the worker to map out everywhere the Atlantic water can reach.
        bfs(atlantic, atl)

        # 5. FIND THE WINNERS
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                # Look at both maps we created. 
                # If a spot is marked 'True' for BOTH oceans, it's a winner!
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
                    
        return res