class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        d = defaultdict()
        d[0] = 0
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        @lru_cache(None)
        def helper(i):
            if i == n:
                return 0
            j = i+1
            # l = i+1
            # r = n-1
            # ans = l
            # while(l < r):
            #     m = (l+r)//2
            #     if jobs[m][0] == jobs[i][1]:
            #         ans = m
            #     elif jobs[m][0] < jobs[i][1]:
            #         l = m + 1
            #     else:
            #         ans = m
            #         r = m - 1
                    
            while (j < n and jobs[j][0] < jobs[i][1]):
                j += 1
            one = jobs[i][2] + helper(j)
            two = helper(i+1)
            return max(one, two)
        return helper(0)
            