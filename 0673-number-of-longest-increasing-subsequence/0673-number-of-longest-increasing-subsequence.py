class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1]*l
        count = [1]*l
        for i in range(0, l):
            for x in range(0, i):
                if nums[x] < nums[i]:
                    if dp[i] == 1+dp[x]:
                        count[i] += count[x]
                    elif dp[i] < dp[x]+1:
                        dp[i] = 1+dp[x]
                        count[i] = count[x]
        maxi = max(dp)
        ans = 0
        for i in range(l):
            if dp[i] == maxi:
                ans += count[i]
        return ans