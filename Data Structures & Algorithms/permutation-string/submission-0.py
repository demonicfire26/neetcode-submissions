class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False
        s1_count = [0] * 26
        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1
        window_count = [0] * 26
        for i in range(len_s2):
            window_count[ord(s2[i]) - ord('a')] += 1
            if i >= len_s1:
                window_count[ord(s2[i - len_s1]) - ord('a')] -= 1
            if window_count == s1_count:
                return True
        return False