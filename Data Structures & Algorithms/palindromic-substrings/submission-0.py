class Solution:
    def countSubstrings(self, s: str) -> int: # Changed name and return type

        def cp(s, left, right):
            L = left
            R = right
            count = 0
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
                count += 1
            
            return count
    
        ans = 0
        for i in range(len(s)):
            ans += cp(s, i, i)
            ans += cp(s, i, i+1)
            
        return ans