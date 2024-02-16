class Solution:
    def trap(self, height: List[int]) -> int:
        # [4,2,0,3,2,5]
        # ans = 9, tmp = 0
        # s= [4, 5]
        l = 0
        r = len(height)-1
        prevL = height[l]
        prevR = height[r]
        ans = 0
        if r == 1:
            return 0
        while l <= r:
            if prevL < prevR:
                if prevL-height[l] > 0:
                    ans += prevL-height[l]
                prevL = max(prevL, height[l])
                l += 1
            else:
                if prevR-height[r] > 0:
                    ans += prevR-height[r]
                prevR = max(prevR, height[r])
                r -=1
        return ans