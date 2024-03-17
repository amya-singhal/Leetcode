class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        ans = []
        """
        n = len(intervals)
        if n == 0:
            return [newInterval]
        ans = []
        i = 0
        for i in range(n):
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans+ intervals[i:]
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        ans.append(newInterval)
        return ans
        