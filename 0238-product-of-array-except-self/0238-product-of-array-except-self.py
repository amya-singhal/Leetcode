class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        ans = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            ans[i] *= left
            left = left*nums[i]
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= right
            right = right*nums[i]
        return ans