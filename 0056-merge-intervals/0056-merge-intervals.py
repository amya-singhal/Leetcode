class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # i < j, if sj <= ei: overlap happens
        # else, add element
        # [1,8],[2,6],[7,10]
        # [1,8], [7,10]
        intervals.sort()
        if len(intervals) == 1:
            return intervals
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][0] = min(merged[-1][0], intervals[i][0])
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
        return merged
    
    # merged --> [[1,6],[8,10],[15,18]]
    # merged --> [[1,5]]
    # [1,8],[2,6],[7,10]
    # merged --> [[1,10]]