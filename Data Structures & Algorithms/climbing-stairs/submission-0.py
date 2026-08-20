class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev1 = 1
        prev2 = 1
        for i in range(1, n):
            current = prev1+prev2
            prev2 = prev1
            prev1 = current

        return prev1
        
            


        
        

        
