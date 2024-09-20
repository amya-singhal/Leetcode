class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i]+1
        for n in nums:
            if abs(n) > len(nums):
                continue
            else:
                nums[abs(n)-1] = -nums[abs(n)-1]
        # print(nums)
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        return len(nums)
             