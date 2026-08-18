from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to check if a given speed k works
        def canFinish(k: int) -> bool:
            total_hours = 0
            for pile in piles:
                # Calculate hours needed for this pile
                total_hours += (pile + k - 1) // k  # Ceiling division
                if total_hours > h:  # Early exit if we exceed h
                    return False
            return total_hours <= h
        
        # Binary search for minimum k
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid  # Try to find smaller k
            else:
                left = mid + 1  # Need larger k
        
        return left