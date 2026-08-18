class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums4 = sorted(nums3)
        n = len(nums4) 
        if n%2 != 0:
            return nums4[n//2]
        else:
            k = (nums4[(n//2)-1]+nums4[(n//2)])/2
            return k
