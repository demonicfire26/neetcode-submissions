class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, num1 in enumerate(nums):
            if num1 == target:
                return i
        return -1


        