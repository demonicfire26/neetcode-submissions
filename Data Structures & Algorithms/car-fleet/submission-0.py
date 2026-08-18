from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create pairs of (position, speed)
        cars = [(position[i], speed[i]) for i in range(len(position))]
        
        # Sort by position in descending order (closest to target first)
        cars.sort(reverse=True)
        
        fleets = 0
        current_time = 0
        
        for pos, spd in cars:
            # Time for this car to reach target if alone
            time = (target - pos) / spd
            
            # If this car takes longer than the fleet ahead, it forms a new fleet
            if time > current_time:
                fleets += 1
                current_time = time
        
        return fleets