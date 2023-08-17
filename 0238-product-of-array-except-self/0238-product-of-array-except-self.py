class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cA = [1]*len(nums)
        y = nums[0]
        for i in range(1, len(nums)):
            cA[i] = y * cA[i]
            y *= nums[i]
        y = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            cA[i] = y *cA[i]
            y *= nums[i]
        
        return cA
                