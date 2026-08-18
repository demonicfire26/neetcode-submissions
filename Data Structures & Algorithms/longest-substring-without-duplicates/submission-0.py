class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}  
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            if s[right] in index_map and index_map[s[right]] >= left:
                left = index_map[s[right]] + 1
            
            index_map[s[right]] = right
            
            current_len = right - left + 1
            max_len = max(max_len, current_len)
        
        return max_len