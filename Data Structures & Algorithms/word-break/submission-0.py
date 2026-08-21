class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        
        # dp[i] represents whether s[0:i] can be segmented into dictionary words
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string is always valid
        
        for i in range(1, n + 1):
            for j in range(i):
                # If s[:j] is valid and the rest s[j:i] is a word in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Found a valid split for index i, move to next
                    
        return dp[n]