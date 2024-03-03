class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        nums = [2,3,1,1,4]
        dp = [2,1,2,1,0]
        """
        dp = [float('inf') for _ in range(len(nums))]
        dp[len(nums)-1] = 0
        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i]):
                if i+j+1 < len(nums):
                    dp[i] = min(dp[i], 1+dp[i+j+1])
        return dp[0]