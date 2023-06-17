class Solution: 
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        if not l:
            return 0
        if l == 1:
            return heights[0]
        stack = []
        maxArea = -float('inf')
        for i, h in enumerate(heights):
            t = i
            while stack and h < stack[-1][1]:
                d, tmpH = stack.pop()
                maxArea = max(maxArea, tmpH*(i - d))
                t = d
            stack.append([t, h])
        while(stack):
            d, tmpH = stack.pop()
            maxArea = max(maxArea, tmpH*(l-d))
        return maxArea
                    