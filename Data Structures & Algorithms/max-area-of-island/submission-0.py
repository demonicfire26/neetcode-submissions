class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # Here we are using DFS approach
        
        # Taking care of the edge cases
        if len(grid) == 0:
            return 0
        # Initialising the variable
        max_area = 0

        # Making the User defined function
        def dfs(grid, i, j):
            # Checking if the given grid is going out of bounds, and if it does we return 0
            if i < 0 or i >= len(grid) or j < 0 or j>= len(grid[i]) or grid[i][j] == 0:
                return 0
            # If it is not out of bounds we mark the cell as 0 in the input to say we have visited this cell
            grid[i][j] = 0
            # Initialising the 'area' variable
            area = 1

            # Here we are going to use the DFS Approach in for 4 directions by using recursion
            area += dfs(grid, i + 1, j)
            area += dfs(grid, i - 1, j)
            area += dfs(grid, i, j + 1)
            area += dfs(grid, i, j - 1)

            return area

        # First loop used to iterarte through the matrix
        for i in range(len(grid)):
            # Second loop ussed to iterate through the first loop matrix
            for j in range(len(grid[i])):
                # Checking if the value is '1'
                if grid[i][j] == 1:
                    # Using a self defined function dfs() to check all the neighbouring nodes from grid[i][j] and calculating the area value
                    area = dfs(grid, i, j)
                    # If the max value is lower than the current area value, the are value become the new max_area 
                    max_area = max(max_area, area)
            
        return max_area

        


            



        
