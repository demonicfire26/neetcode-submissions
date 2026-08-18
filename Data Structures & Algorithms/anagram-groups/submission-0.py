from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to map sorted tuple of characters -> list of anagrams
        anagram_map = {}
        
        for s in strs:
            # Sort the string to get a canonical key for anagrams
            # For example, "eat" and "tea" both become ['a','e','t']
            key = tuple(sorted(s))
            
            # If the key is not in the map, create a new list
            if key not in anagram_map:
                anagram_map[key] = []
            
            # Append the original string to the corresponding group
            anagram_map[key].append(s)
        
        # Return all the grouped anagrams as a list of lists
        return list(anagram_map.values())