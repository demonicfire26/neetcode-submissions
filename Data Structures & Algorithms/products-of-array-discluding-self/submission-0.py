class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #creating a new list
        new_list = []

        for i in range(len(nums)):

            #calculating the products on the left side of the integer
            left = math.prod(nums[0:i])

            #calculating the products on the right side of the integer
            right = math.prod(nums[i+1:])

            #multiplying both
            new_list.append(left*right)
        return new_list
        