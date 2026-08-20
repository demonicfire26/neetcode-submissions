
class Solution:
    # dw => distinct ways
    # as n = 0, distinct ways = 1
    # as n = 1, distinct ways = 1
    # as n = 2, distinct ways = 2
    # as n = 3, distinct ways = 3
    # as n = 4, distinct ways = 5
    #by looking at the values we get the mathematical formula: 
    #dw(i) = dw(i-1) + dw(i-2)
    def climbStairs(self, n: int) -> int:
        #baseline results
        if n == 0 or n == 1:
            return 1
        # initiating the first values
        prev1 = 1
        prev2 = 1
        # we make a 'for' loop to iterate through the numbers unitl n value 
        for i in range(1, n):
            #current result is sum of previous 2 results
            current = prev1+prev2
            # changing the values of the previous 2 results to the current ones to calculate the next values
            prev2 = prev1
            prev1 = current

        return prev1
        
            


        
        

        
