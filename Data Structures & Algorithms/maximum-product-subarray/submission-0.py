class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprod = 1
        maxprod = 1
        result = nums[0]

        for i in range(len(nums)):
            temp = maxprod*nums[i]
            maxprod = max(nums[i], max(nums[i]*maxprod, nums[i]*minprod))
            minprod = min(nums[i], min(temp , minprod*nums[i]))

            result = max(result, max(maxprod, minprod))

        return result