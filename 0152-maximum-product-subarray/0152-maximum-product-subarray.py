class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        localMax, localMin = maxi, maxi
        for i in range(1, len(nums)):
            if (nums[i] < 0):
                localMax, localMin = localMin, localMax
            localMax = max(nums[i], nums[i]*localMax)
            localMin = min(nums[i], nums[i]*localMin)
            maxi = max(localMax, maxi)
        return maxi
        