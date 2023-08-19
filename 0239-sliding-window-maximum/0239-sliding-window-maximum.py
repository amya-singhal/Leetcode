class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = []
        i = 0
        for i in range(len(nums)):
            if len(q) and q[0] == i-k:
                q.pop(0)
            while len(q) and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k-1:
                ans.append(nums[q[0]])
            # print(q)
        return ans
        