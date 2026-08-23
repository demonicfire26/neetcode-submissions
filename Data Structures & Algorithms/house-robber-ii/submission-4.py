class Solution:
    def rob(self, nums: List[int]) -> int:

        # Initialsing the values
        rob1 = 0
        rob2 = 0
        max1 = 0

        rob3 = 0
        rob4 = 0
        max2 = 0
        if len(nums) == 1:
            max1 = nums[0]
        
            


        #Making the 'for' loop
        for i in range(len(nums)-1):
            # Using the Mathematical Formula
            max1 = max(rob1 + nums[i], rob2)
            # Changing the values to check on other possibilities
            rob1 = rob2
            rob2 = max1
        
        for i in range(1, len(nums)):
            # Using the Mathematical Formula
            max2 = max(rob3 + nums[i], rob4)
            # Changing the values to check on other possibilities
            rob3 = rob4
            rob4 = max2
        

        return max(max1, max2)