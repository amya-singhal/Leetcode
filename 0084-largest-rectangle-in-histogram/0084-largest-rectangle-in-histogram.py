class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(0, len(heights)):
            if not stack:
                stack.append([heights[i], i])
            else:
                tmp = i
                while(stack and stack[-1][0] > heights[i]):
                    x, y = stack.pop()
                    maxArea = max(maxArea, x*(i-y))
                    tmp = y
                stack.append([heights[i], tmp])
        n = len(heights)
        while(stack):
            x, y = stack.pop()
            maxArea = max(maxArea, x*(n-y))
            
        return maxArea