class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        # [1,-1]
        # 1
        # heap = [5, ]
        # ans = [3, 3, 5]
        for i in range(k):
            while heap and nums[heap[-1]] < nums[i]:
                heap.pop()
            heap.append(i)
        ans.append(nums[heap[0]])  
        for i in range(k, len(nums)):
            if heap[0] == i-k:
                heap.pop(0)
            while heap and nums[heap[-1]] < nums[i]:
                heap.pop()
            heap.append(i)
            ans.append(nums[heap[0]])
        return ans
            