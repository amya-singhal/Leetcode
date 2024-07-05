class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        mergedIntervals = [intervals[0]]
        lIntervals = len(intervals)
        for start, end in intervals:
            mergedS, mergedE = mergedIntervals.pop()
            if start <= mergedE:
                mergedIntervals.append([min(mergedS, start), max(mergedE, end)])
            else:
                mergedIntervals.append([mergedS, mergedE])
                mergedIntervals.append([start, end])
        return mergedIntervals
            