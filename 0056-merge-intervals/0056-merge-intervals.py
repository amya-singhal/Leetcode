class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergeIntervals = []
        tmp = [intervals[0][0], intervals[0][1]]
        for i in range(1, len(intervals)):
            if intervals[i-1][1] >= intervals[i][0]:
                e = max(intervals[i][1], intervals[i-1][1])
                intervals[i][1] = e
                if len(tmp) == 0:
                    tmp.append(intervals[i-1][0])
                    tmp.append(e)
                else:
                    tmp[1] = e
            else:
                mergeIntervals.append(tmp)
                tmp = []
                tmp.append(intervals[i][0])
                tmp.append(intervals[i][1])
        if len(tmp) != 0:
            mergeIntervals.append(tmp)
        return mergeIntervals
                
        