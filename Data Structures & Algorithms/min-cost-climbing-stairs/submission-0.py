class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return None
        elif len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost[0], cost[1])
        prev1 = cost[0]
        prev2 = cost[1]
        n = len(cost)
        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev1 = prev2
            prev2 = current
        
        return min(prev1, prev2)
        