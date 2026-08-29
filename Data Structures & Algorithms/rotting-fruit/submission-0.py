class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Here we are using a BFS approach on an adjacency matrix, and whenever we make a new BFS call, we increment the minute counter
        # Also, we need to check the positions where the rotten fruits are present as to determine from wherre we will start our graph traversals
        # To use BFS, we need a queue
        
        # Handling the edge cases
        if len(grid) == 0:
            return 0
        
        # Assigning the values
        m =len(grid) # Number of Rows
        n = len(grid[0]) # Number of Columns

        # Making the fresh fruit counter
        fresh = 0

        # Initialising the queue to store all the rotten fruits found so far
        rottenQueue = deque()

        # Now we use 2 for loops to cehck if there are fresh and rotten friuts preent in the matrix

        # First loop used to iterate through the Columns
        for i in range(m):
            # Second loop used to iterate through the Rows
            for j in range(n):

                # If the node contains a fresh fruit, we increment the 'fresh' counter 
                if grid[i][j] == 1:
                    fresh += 1
                
                # If the node contains a rotten fruit, we append that node into the 'rottenQueue' queue
                elif grid[i][j] == 2:
                    rottenQueue.append((i, j))

        # If the there are no fresh fruits, we return 0
        if fresh == 0:
            return 0

        # Initialising the minute counter
        minutes = 0

        # Initialising a directional array to iterate over all 4 directions for any particular node
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Starting the BFS approach

        # Making a while loop where the condition is rottenQueue is not empty
        while rottenQueue:

            # Making the queue size
            size = len(rottenQueue)

            # for loop to iterate through the queue
            for i in range(size):

                # We pop one element out and marking it as rotten and start our BFS approach from there
                rotten = rottenQueue.popleft()

                # We use another for loop to iterate in all 4 directions from the 'rotten' node using the 'directions' array
                for dire in directions:

                    # Calculating the x and y positons of the adjacent nodes from the 'rotten' node
                    x = rotten[0] + dire[0]
                    y = rotten[1] + dire[1]

                    # Checking if we are not going out of the martix or not out of bounds
                    if x >= 0 and x < m and y >= 0 and y < n and grid [x][y] == 1:

                        # If we are not out of bounds, thenwe will be turing the fresh fruits into rotten fruits
                        grid[x][y] = 2

                        # Decrement the fresh fruit counter
                        fresh -= 1

                        # Now we will be adding the position of the newly rotten fruit in the 'rottenQueue' queue
                        rottenQueue.append((x,y))

            # Now we increment the minute counter if the queue has been repopulated with new rotten oranges
            if rottenQueue:
                minutes += 1

        # Making sure if there are not fresh fruits left
        if fresh == 0:
            return minutes

        # If there are still some fresh fruits, we return '-1'
        else:
            return -1













