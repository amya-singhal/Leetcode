class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums))
        for i in reversed(range(0, len(nums) - 1)):
            for x in range(i+1, len(nums)):
                if(nums[x] > nums[i]):
                    dp[i] = max(dp[x] + 1, dp[i])
        return max(dp)   
            