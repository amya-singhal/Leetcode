class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) == len(set(nums)):
            return []
        ans = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]
        return ans
            