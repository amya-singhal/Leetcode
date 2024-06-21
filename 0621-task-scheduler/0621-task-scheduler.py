class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        h = list(d.values())
        h = [-x for x in h]
        heapq.heapify(h)
        ans = 0
        while h:
            # print(h, ans)
            tmp = []
            for _ in range(n+1):
                # print(h)
                if h:
                    x = heappop(h)
                    x += 1
                    if x != 0:
                        tmp.append(x)
                ans += 1
                if not h and not tmp:
                    return ans
            for t in tmp:
                heappush(h, t)
        return ans
        