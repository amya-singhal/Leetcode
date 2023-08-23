class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        mergeIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > mergeIntervals[-1][1]:
                mergeIntervals.append(intervals[i])
            else:
                new = [min(intervals[i][0], mergeIntervals[-1][0]), max(intervals[i][1], mergeIntervals[-1][1])]
                mergeIntervals.pop()
                mergeIntervals.append(new)
        return mergeIntervals
                
        