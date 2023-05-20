class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for (x, y) in points:
            dist = x*x + y*y
            min_heap.append([dist, x, y])
        
        heapq.heapify(min_heap)
        ans = []
        while (k):
            dist, x, y = heapq.heappop(min_heap)
            ans.append([x, y])
            k -= 1
        return ans