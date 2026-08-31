class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Here we areusing DFS approach
        # In this scenario, we traverse the grid until we reach an island, and when we reach it, we push this island in the water by marking to '0'. Then we look at all 4 directions from that sunken island to check if there are any other island right beside it. If it is there we push that island too in the water. We repeat this process using recursion to every adjacent island until we find no other connected island. Here we increment the island counter by 1 stating we have found 1 group of islands. We repeat this process over the whole grid till we sink all the ilands and have the final count of the number of islands in the grid.

        # Initialising the directions list
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        #Initialising the rows and columns variables
        ROWS, COLS = len(grid), len(grid[0])

        # Initialising the island counter
        islands = 0
        
        # We define the island sinking function where 'r' and 'c' are the positions of the island node
        def dfs(r, c):

            # Checking if we are going out of bounds or the node we are looking at is a water body, in which case we return nothing
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return

            # We push that island node into the water by changing it value to '0'
            grid[r][c] = "0"

            # Making a for loop to check in all 4 directions from the sunken island node
            for dr, dc in directions:

                # Using the recursion to do the whole process again
                dfs(r + dr, c + dc)

        # We are using 2 for loops to traverse trhough the whole adjacency matrix
        for r in range(ROWS):
            for c in range(COLS):

                # If the node we are looking at is a island node, we call the island sinking function and increment the island counter by 1
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        # We return the final count from the island counter          
        return islands