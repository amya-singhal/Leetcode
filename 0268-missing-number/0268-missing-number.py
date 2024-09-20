class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        reqTotal = ((n+1)*n) / 2
        for num in nums:
            reqTotal -= num
        return int(reqTotal)