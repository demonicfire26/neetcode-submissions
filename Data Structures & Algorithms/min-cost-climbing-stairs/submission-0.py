class Solution:
    # the mathematical formula is :
    # cost till (i))th value = (cost at i + min(cost till (i-1)th value, cost till (i-2)th value)
    # The final cost will be min(cost till (n-1)th value, cost till (n)th value)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        #baseline results
        if n == 1:
            return cost[0]
        elif n == 2:
            return min(cost[0], cost[1])
        # initialising the values
        prev1 = cost[0]
        prev2 = cost[1]
        # making the for loop to iterate through the list
        for i in range(2, n):
            # implementing the formula
            current = cost[i] + min(prev1, prev2)
            # assigning the new values
            prev1 = prev2
            prev2 = current

        return min(prev1, prev2)
