class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if not prices:
            return 0
       
        for i in range(len(prices)-1):
            lowest_cost = prices[i]
            highest_cost = max(prices[i+1:])
            max_profit = max(max_profit, highest_cost - lowest_cost)

        return max_profit