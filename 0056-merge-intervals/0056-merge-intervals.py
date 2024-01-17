class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        # sorting using start time
        intervals.sort()
        print(intervals)
        merge_intervals = [intervals[0]] #[[0,0]]
        for i in range(1, len(intervals)):
            start, end = merge_intervals[-1] #0,0
            next_start = intervals[i][0] #1
            print(start, end, next_start)
            if next_start <= end:
                merge_intervals.pop()
                merge_intervals.append([min(start, intervals[i][0]), max(intervals[i][1], end)])
            else:
                merge_intervals.append(intervals[i])
        return merge_intervals
            
        