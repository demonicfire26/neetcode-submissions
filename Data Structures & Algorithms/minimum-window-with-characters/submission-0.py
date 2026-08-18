class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        have = {}           
        need_count = len(need)    
        have_count = 0            
        left = 0
        min_len = float('inf')
        min_start = 0
        for right in range(len(s)):
            char = s[right]
            have[char] = have.get(char, 0) + 1
            if char in need and have[char] == need[char]:
                have_count += 1
                
            while have_count == need_count:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_start = left
                left_char = s[left]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    have_count -= 1
                left += 1
        return s[min_start:min_start + min_len] if min_len != float('inf') else ""
        