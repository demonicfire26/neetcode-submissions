class Solution:
    def numDecodings(self, s: str) -> int:
        prev1 = 1
        prev2 = 1
        if not s or s[0] == '0':
            return 0
        for i in range(1, len(s)):
            res = 0
            
            if s[i] != '0':
                res +=prev1
            two_digit = int(s[i-1:i+1])
            if two_digit <= 26 and two_digit >= 10:
                res +=prev2
                
            elif res == 0:
                return 0
            
            prev2 = prev1
            prev1 = res
        


        return prev1

        