class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [2,0,2,1,1,0]
        lengthNums = len(nums)
        left, right = 0, lengthNums-1
        i = 0
        while(i <= right):
            color = nums[i]
            if color == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif color == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
            
        