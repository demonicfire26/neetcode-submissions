class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        l_length = 0
        for i in my_set:
            if i-1 not in my_set:
                new_num = i
                length = 1
                while new_num+1 in my_set:
                    new_num+=1
                    length+=1
                l_length = max(l_length, length)
        return l_length
                


        