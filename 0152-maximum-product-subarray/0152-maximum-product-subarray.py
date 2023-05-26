class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        localMax, localMin = maxi, maxi
        for i in range(1, len(nums)):
            tmp = localMax*nums[i]
            localMax = max(nums[i], tmp, localMin*nums[i])
            localMin = min(nums[i], nums[i]*localMin, tmp)
            maxi = max(localMax, maxi)
        return maxi
        