class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        currentMax = 0
        l = 0
        r = len(height) - 1
        while(l <= r):
            currentMax = (r-l) * min(height[l], height[r])
            maxArea = max(currentMax, maxArea)
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return maxArea