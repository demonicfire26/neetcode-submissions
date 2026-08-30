class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # Here we are going to start from the treasure node and start incrementing the counter everytime we meet a island node through BFS approach from the treasure node. After getting the different distance from the different treasure nodes into the island node, we then find the minimum distances from the ones stored in the island nodes. We need to make a queue to keep a track of all the island nodes we have visited, as to not visit them again during BFS approach.

        # Making the infinity number and the directions
        INF = 2147483647
        DIRS = [0, 1, 0, -1, 0]

        # Checking if the grid is not there or nothing is present in the list
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return

        # Making the number of rows and columns variables
        m = len(grid) # Number of rows
        n = len(grid[0]) # Number of columns

        # Queue used for BFS approach
        queue = deque()

        # Making 2 for loops to find all the treasure nodes in the grid and put it in the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))

        # Now we do BFS from each treasure node
        while queue:

            # Taking the first treasure node from the queue
            treasure = queue.popleft()

            # Position of the treasure node
            row = treasure[0]
            col = treasure[1]

            # From the treasure node position, we will now check in which 4 directions we can explore into
            for i in range(4):
                newRow = row + DIRS[i]
                newCol = col + DIRS[i + 1]

                # Now for each direction, we are going to check 1) we are not going out of bounds, 2) If the value in the node we are reaching has the 'INF' value
                if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n and grid[newRow][newCol] == INF:

                    # If all conditions are met, we update the distance from the treasure node in this island node by incrementing by 1 from the previous island node
                    grid[newRow][newCol] = grid[row][col] + 1

                    # Now we add the distance in the island node in the queue
                    queue.append((newRow, newCol))
        
        



