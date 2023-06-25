class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        points_s = sorted(points, key = lambda x: x[1])
        end = points_s[0][1]
        for x, y in points_s[1:]:
            if end < x: 
                ans += 1
                end = y
        return ans
        