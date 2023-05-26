class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if (l == 1):
            return nums[0]
        if (l == 0):
            return 0
        ans = [0] * (l)
        ans[0] = nums[0]
        ans[1] = max(nums[0], nums[1])
        for i in range (2, len(nums)):
            ans[i] = max(ans[i-2], ans[i-2] + nums[i], ans[i-1])
        return max(ans)
        