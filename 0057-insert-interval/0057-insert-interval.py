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
        used = 0
        mergedInt = []
        for x,y in intervals:
            if y < newInterval[0] or x > newInterval[1]:
                mergedInt.append([x,y])
            else:
                if used == 0:
                    mergedInt.append([min(x, newInterval[0]), max(y, newInterval[1])])
                    used = 1
                else:
                    i, j = mergedInt.pop()
                    mergedInt.append([min(i, x), max(j, y)])
        if used == 0:
            mergedInt.append(newInterval)
            mergedInt = sorted(mergedInt)
        return mergedInt