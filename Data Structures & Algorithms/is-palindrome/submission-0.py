class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = re.sub(r'[^a-zA-Z0-9 ]', '', s)
        s1 = s2.lower()
        new_s = s1.replace(" ","")
        r_new_s = new_s[::-1]
        print(r_new_s)
        print(new_s)
        if new_s == r_new_s:
            return True
        else:
            return False
        