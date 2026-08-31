from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        
        # Here we are using the BFS approach where we change the combination of the 'beginWord' according to the rules and check if these combinations are present in the dictionary, if it is there, we see there new combinations in the dictionary too until we get the 'endWord'. When we reach the 'endWord',we look at the path which takes the minimum words to reach the 'endWord' 

        # 1. THE IMPOSSIBLE CHECKS
        # If the word we are trying to reach isn't even in the allowed dictionary, 
        # or if we are already at the end word, we can't play the game. Return 0.
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
            
        # 2. SETUP THE GAME
        # Turn the dictionary into a 'set' (a hash map). This makes checking if a word 
        # exists lightning fast! We also start our step counter (res) at 0.
        words = set(wordList)
        res = 0
        
        # Make a waiting line for the words we are currently testing.
        q = deque([beginWord])
        
        # 3. PLAYING THE GAME (Level by Level)
        while q:
            # We are taking 1 full step forward in our game.
            res += 1
            
            # Look at exactly how many words are in the line right now. 
            # We only want to test this specific batch of words for this step.
            for _ in range(len(q)):
                
                # Take the next word out of the front of the line.
                node = q.popleft()
                
                # WIN CONDITION: If this word matches our goal, we are done! 
                # Return the number of steps it took.
                if node == endWord:
                    return res
                    
                # 4. THE MUTATION STATION
                # Go through every single letter slot in the current word.
                for i in range(len(node)):
                    
                    # Try replacing that letter with every letter in the alphabet (a to z).
                    # (Numbers 97 to 123 are the computer codes for 'a' to 'z').
                    for c in range(97, 123):
                        
                        # If the new letter is exactly the same as the old letter, skip it.
                        if chr(c) == node[i]:
                            continue
                            
                        # Glue the word back together with the one new letter swapped in.
                        nei = node[:i] + chr(c) + node[i + 1:]
                        
                        # 5. CHECK THE DICTIONARY
                        # Is this newly mutated word a valid word in our allowed list?
                        if nei in words:
                            # It is valid! Add it to the waiting line for the next round.
                            q.append(nei)
                            
                            # CRITICAL STEP: Cross this word out of the dictionary completely!
                            # This stops us from accidentally walking backwards in a circle later.
                            words.remove(nei)
                            
        # If the waiting line completely empties out and we never found the end word, 
        # it means the transformation is impossible. Return 0.
        return 0