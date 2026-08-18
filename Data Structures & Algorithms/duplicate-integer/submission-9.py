class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = sorted(nums)
        for i in range(1, len(new_nums)):
            if new_nums[i] == new_nums[i-1]:
                return True

        return False

        