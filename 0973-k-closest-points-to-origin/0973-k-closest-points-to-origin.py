class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        dic = defaultdict(list)
        for x, y in points:
            d = x*x + y*y
            dic[d].append([x, y])
            heapq.heappush(heap, d)
        answer = []
        while (k > 0):
            d = heapq.heappop(heap)
            values = dic[d]
            for x,y in values:
                answer.append([x,y])
                k -= 1
        return answer