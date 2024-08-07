class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lNums = len(nums)
        dp = [0 for _ in range(lNums)]
        dp[0] = nums[0]
        for i in range(1, lNums):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)
            
            
        