class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftP = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            leftP[i] = leftP[i-1]*nums[i-1]
        # [1,1,2,6]
        rightP = [1 for _ in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            rightP[i] = rightP[i+1]* nums[i+1]
        # [24,12,4,1]
        ans = []
        for i in range(len(nums)):
            ans.append(leftP[i]*rightP[i])
        return ans