class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        sorted_s = sorted(list_s)
        sorted_t = sorted(list_t)
        if sorted_s == sorted_t:
            return True
        return False

        