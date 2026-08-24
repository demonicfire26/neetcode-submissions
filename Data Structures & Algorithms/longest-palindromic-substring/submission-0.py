class Solution:
    def longestPalindrome(self, s: str) -> str:

        def cp(s, left, right):
            L = left
            R = right
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            
            return R - L - 1
        
    

        if len(s) == 0:
            return 0
        left = 0
        right = 0
        for i in range(len(s)):
            len1 = cp(s, i, i)
            len2 = cp(s, i, i+1)
            len3 = max(len1, len2)

            if len3 > (right - left):
                left = i - (len3 - 1) // 2
                right = i + len3 // 2

        return s[left : right + 1]
        