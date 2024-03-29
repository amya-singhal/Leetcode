class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        while(k):
            x = heapq._heappop_max(nums)
            k -= 1
        return x