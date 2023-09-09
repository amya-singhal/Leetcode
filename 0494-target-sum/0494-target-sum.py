class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def helper(index, currentSum):
            nonlocal dp
            if index == len(nums):
                if currentSum == target:
                    return 1
                return 0
            if (index, currentSum) in dp:
                return dp[(index, currentSum)]
            dp[(index, currentSum)] = (helper(index+1, currentSum+nums[index]) + helper(index+1, currentSum-nums[index]))
            return dp[(index, currentSum)]
        return helper(0, 0)
