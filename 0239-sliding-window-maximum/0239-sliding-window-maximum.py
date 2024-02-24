class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = deque()
        ans = []
        l = 0
        # [1,-1]
        # 1
        # heap = [5, ]
        # ans = [3, 3, 5]
        for i in range(k):
            while heap and heap[-1] < nums[i]:
                heap.pop()
            heap.append(nums[i])
        ans.append(heap[0])  
        for i in range(k, len(nums)):
            if heap[0] == nums[l]:
                heap.popleft()
            while heap and heap[-1] < nums[i]:
                heap.pop()
            heap.append(nums[i])
            ans.append(heap[0])
            l += 1
        return ans
            