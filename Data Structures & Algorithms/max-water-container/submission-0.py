from itertools import combinations
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_vol = 0
        for (i, h1), (j, h2) in combinations(enumerate(heights), 2):
            volume = min(h1, h2) * abs(j - i)
            max_vol = max(max_vol, volume)
        return max_vol