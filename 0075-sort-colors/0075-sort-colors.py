class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cr, cw, cb = 0, 0, 0
        for n in nums:
            if n == 0:
                cr += 1
            elif n == 1:
                cw += 1
            else:
                cb += 1
        for i in range(0, len(nums)):
            if cr:
                nums[i] = 0
                cr -= 1
            elif cw:
                nums[i] = 1
                cw -= 1
            else:
                nums[i] = 2
                cb -= 1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        