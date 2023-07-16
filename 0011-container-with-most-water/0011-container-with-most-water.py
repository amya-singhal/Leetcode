class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        currA = 0
        l = 0
        r = len(height) - 1
        while(l <= r):
            currA = (r-l)* min(height[l], height[r])
            maxA = max(maxA, currA)
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return maxA
            