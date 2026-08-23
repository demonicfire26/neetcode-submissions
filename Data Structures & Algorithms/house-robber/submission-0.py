class Solution:
    def rob(self, nums: List[int]) -> int:

        # Initialsing the values
        rob1 = 0
        rob2 = 0
        max1 = 0
        #Making the 'for' loop
        for i in range(len(nums)):
            # Using the Mathematical Formula
            max1 = max(rob1 + nums[i], rob2)
            # Changing the values to check on other possibilities
            rob1 = rob2
            rob2 = max1

        return max1