class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        for i in range(len(nums)):
            if len(heap) and heap[0] == i-k:
                heap.pop(0)
            while len(heap) and nums[i] > nums[heap[-1]]:
                heap.pop()
            heap.append(i)
            if i >= k-1:
                ans.append(nums[heap[0]])
            # print(heap)
        return ans
            