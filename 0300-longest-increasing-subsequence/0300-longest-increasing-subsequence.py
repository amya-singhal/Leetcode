class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        a = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i] and a[j] + 1 > a[i]:
                    a[i] = a[j] + 1
        
        return max(a)
        