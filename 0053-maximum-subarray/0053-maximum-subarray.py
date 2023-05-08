class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        maxSum = nums[0]
        for n in range(1, len(nums)):
            maxi = max(maxi+nums[n], nums[n])
            maxSum = max(maxSum, maxi)
        return maxSum
        