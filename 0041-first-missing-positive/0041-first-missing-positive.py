class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        oneExists = False
        for i in nums:
            if i == 1:
                oneExists = True
        if not oneExists:
            return 1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        for i in range(len(nums)):
            x = abs(nums[i]) - 1
            if 0 <= x < len(nums):
                nums[x] = - abs(nums[x])
        # print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1
            