from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Handle edge case: empty matrix
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Step 1: Find the row that might contain the target
        top = 0
        bottom = rows - 1
        
        while top <= bottom:
            mid_row = (top + bottom) // 2
            
            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else:
                # Target is within this row's range
                # Step 2: Binary search within the row
                left = 0
                right = cols - 1
                
                while left <= right:
                    mid_col = (left + right) // 2
                    
                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif matrix[mid_row][mid_col] < target:
                        left = mid_col + 1
                    else:
                        right = mid_col - 1
                
                return False
        
        return False