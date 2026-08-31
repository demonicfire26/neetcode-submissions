class Solution:

    def encode(self, strs: list[str]) -> str:
        
        # 1. SETUP: We are packing a bunch of separate words into one giant shipping box (a single string).
        encoded_str = ""
        
        # We use a special "|" sticker to separate our instruction label from the actual word.
        delimeter = "|"
        
        # Look at every single word in our list one by one.
        for i in strs:
            # Count exactly how many letters are in this specific word.
            len_str = len(i)
            
            # Glue it all together! 
            # Example: If the word is "cat", we add "3|cat" to our giant box.
            # This way, even if the word itself has weird spaces or symbols, we always know it is exactly 3 letters long.
            encoded_str = encoded_str + str(len_str) + delimeter + i
            
        return encoded_str


    def decode(self, s: str) -> list[str]:
        
        # 2. UNPACKING: We have the giant string and need to pull the original words back out.
        # 'i' is our reading finger. We start pointing at the very beginning (position 0).
        i = 0
        
        # Make an empty list to hold our unpacked words.
        result = []
        
        # Keep reading as long as our finger hasn't reached the end of the giant string.
        while i < len(s):
            
            # Step A: Find the instruction label.
            # Look for the very next "|" sticker, starting from wherever our finger is currently pointing.
            delim_pos = s.find("|", i)
            
            # The number right before the "|" tells us exactly how many letters make up the next word.
            length = int(s[i:delim_pos])
            
            # Step B: Pull out the word.
            # The actual word starts exactly one space after the "|" sticker.
            string_start = delim_pos + 1
            
            # We calculate where the word ends by adding the length we just read.
            string_end = string_start + length
            
            # Slice out the exact word using those start and end points.
            decode = s[string_start:string_end]

            # Put the unpacked word safely into our final list.
            result.append(decode)
            
            # Step C: Move to the next item.
            # Jump our reading finger straight to the end of the word we just pulled out, 
            # so it is perfectly in place to read the number for the next word!
            i = string_end

        return result