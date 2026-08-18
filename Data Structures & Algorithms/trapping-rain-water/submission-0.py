class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        l = 0
        r = 0
        for i in range(len(height)):
            if i==0:
                l = 0
            else:
                l = max(height[0:i])
            if i==len(height)-1:
                r = 0
            else:
                r = max(height[i+1:])
            vol += max(0, min(l,r) - height[i])
        return vol



        