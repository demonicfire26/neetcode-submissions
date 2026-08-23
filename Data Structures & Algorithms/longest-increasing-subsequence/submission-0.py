class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        Lis = [1] * len(nums)
        max_val = 1  
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    Lis[i] = max(Lis[i], 1 + Lis[j])
                    max_val = max(max_val, Lis[i])
        
        return max_val