class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        a = [float("inf")]*(n+1)
        a[0] = 0
        a[k] = 0
        for i in range(0, n):
            for x,y,t in times:
                if a[x] + t < a[y]:
                    a[y] = a[x] + t
        print(a)
        for i in a:
            if i == float("inf"):
                return -1
        return max(a)
        