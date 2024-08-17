class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [[1,2],[2,3],[3,4],[1,3]]
        [[1,2],[1,3],[2,3],[3,4]]
        [[1,10],[2,4][5,7]]
        """
        ans = 0
        sortedIntervals = sorted(intervals)
        dp = {}
        prevS, prevE = sortedIntervals[0][0], sortedIntervals[0][1]
        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[i][0] >= prevE:
                prevE = sortedIntervals[i][1]
            else:
                ans += 1
                prevE = min(prevE,sortedIntervals[i][1])
        return ans