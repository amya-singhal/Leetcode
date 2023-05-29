class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = []
        maxi.append(nums[0])
        for n in range(1, len(nums)):
            x = max(maxi[n-1]+nums[n], nums[n])
            maxi.append(x)
        maxSubArray = maxi[0]
        return max(maxi)