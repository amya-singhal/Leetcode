class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        points_s = sorted(points, key = lambda x: x[0])
        end = points_s[0][1]
        for x, y in points_s[1:]:
            if end >= x: 
                end = min(end, y)
            else:
                ans += 1
                end = y
        return ans
        