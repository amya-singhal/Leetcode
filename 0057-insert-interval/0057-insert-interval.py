class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        while i < len(intervals):
            if (newInterval[1] < intervals[i][0]):
                ans.append(newInterval)
                return ans + intervals[i:]
            elif (intervals[i][1] < newInterval[0]):
                ans.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max (intervals[i][1], newInterval[1])]
            i += 1
        ans.append(newInterval)
        return ans
        