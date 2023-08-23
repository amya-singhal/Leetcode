class Solution:
    def trap(self, height: List[int]) -> int:
        # 
        if not height:
            return 0
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        ans = 0
        while l < r:
            # minH = min(maxL, maxR)
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                ans += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                ans += maxR - height[r]
        return ans
            
                