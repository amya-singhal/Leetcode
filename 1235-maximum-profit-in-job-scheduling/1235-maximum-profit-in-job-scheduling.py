class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)

        def helper(val: int) -> int:
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) >> 1
                s, e, p = jobs[m]
                if s < val: l = m + 1
                else: r = m - 1
            return l

        @cache
        def dp(i: int) -> int:
            if i >= n: return 0
              
            j = helper(jobs[i][1])
            return max(dp(i + 1), dp(j) + jobs[i][2])

        return dp(0)