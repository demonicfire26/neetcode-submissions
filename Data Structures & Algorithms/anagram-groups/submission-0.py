class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        # 1. SETUP THE SHELF
        # We make an empty dictionary. Think of this as a shelf where we will store 
        # different boxes of words. Each box will have a special label on it.
        anagram_map = {}
        
        # 2. SORTING THE WORDS
        # We look at every single word in our list, one by one.
        for s in strs:
            
            # We take the word and put its letters in alphabetical order to make a "secret code".
            # For example, "eat", "tea", and "ate" all get the exact same secret code: ('a', 'e', 't').
            # We use a 'tuple' (parentheses) because Python needs the label on the box to be permanent.
            key = tuple(sorted(s))
            
            # If we haven't seen this secret code before, we put a brand new, empty box on the shelf for it.
            if key not in anagram_map:
                anagram_map[key] = []
            
            # We toss the original word into the box that matches its secret code.
            anagram_map[key].append(s)
        
        # 3. HAND IN THE RESULT
        # We take all the separate boxes off the shelf and hand them back as a final list of groups.
        return list(anagram_map.values())