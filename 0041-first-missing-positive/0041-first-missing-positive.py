class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        [2,4,0,1,5]
        ans = 1
        
        """
        first = False
        for i in range(len(nums)):
            if nums[i] == 1:
                first = True
        if not first:
            return 1
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = 1
        for i in range(len(nums)):
            x = abs(nums[i]) - 1
            if 0 <= x < len(nums):
                nums[x] = - abs(nums[x])
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1
            
        