class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        [3,4,-1,1]
        [1,4,3,-1]
        ans = 1
        l = 4
        i = 0->1->2->3->4
        """
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == i+1 or nums[nums[i]-1] == nums[i]:
                i += 1
            else:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for j in range(len(nums)):
            if nums[j] != j+1:
                return j+1
        return len(nums)+1
        