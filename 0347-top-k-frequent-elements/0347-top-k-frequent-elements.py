class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        heap = [(-value, key) for key,value in d.items()]
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            x = heappop(heap)
            ans.append(x[1])
        return ans
        