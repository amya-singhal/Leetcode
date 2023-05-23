class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        x = 0
        while (x <= right):
            if (nums[x] == 0):
                nums[x], nums[left] = nums[left], nums[x]
                left += 1
                x += 1
            elif (nums[x] == 2):
                nums[x], nums[right] = nums[right], nums[x]
                right -= 1
            else:
                x += 1
        """
        Do not return anything, modify nums in-place instead.
        """
        