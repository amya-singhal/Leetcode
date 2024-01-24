class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        l = 0
        r = len(nums)-1
        x = 0
        while x <= r:
            if nums[x] == 0:
                nums[x], nums[l] = nums[l], nums[x]
                l += 1
                x += 1
            elif nums[x] == 2:
                nums[x], nums[r] = nums[r], nums[x]
                r -= 1
            else:
                x += 1
        
            
            